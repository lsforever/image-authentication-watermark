import numpy as np
import cv2
import pywt
from PIL import Image


k_g = 0.85
q_g = 0.009


# Images should be same lenght and height
# This only uses grascale not full rgba
def embedWatermarkGrayScale(mainImg, markImg, k=k_g, q=q_g):
    main_image_gray_array = np.mean(mainImg, -1)
    mark_image_gray_array = np.mean(markImg, -1)
    
    

    main_image_dwt = pywt.dwt2(main_image_gray_array, 'haar')
    LL, (LH, HL, HH) = main_image_dwt

    mark_image_dwt = pywt.dwt2(mark_image_gray_array, 'haar')
    mLL, (mLH, mHL, mHH) = mark_image_dwt

    # Apla Blend
    marked_LL = k*(LL) + q*(mLL)

    marked_dwt = marked_LL, (LH, HL, HH)
    water_marked_img = pywt.idwt2(marked_dwt, 'haar')

    # items = [
    #     Image.fromarray(main_image_dwt),
    #     Image.fromarray(mark_image_dwt),
    #     Image.fromarray(water_marked_img)
    # ]


    items = [
        Image.fromarray(np.uint8(LH)),
        Image.fromarray(LH),
        Image.fromarray(water_marked_img)
    ]

    return items

# Images should be same lenght and height
# This only uses grascale not full rgba
def extractWatermarkGrayScale(mainImg, waterMarkedImg, k=k_g, q=q_g):
    main_image_gray_array = np.mean(mainImg, -1)
    water_marked_image_gray_array = np.array(waterMarkedImg)
    
    # dwt algorith
    waterMarkedImg_dwt = pywt.dwt2(water_marked_image_gray_array, 'haar')
    wLL, (wLH, wHL, wHH) = waterMarkedImg_dwt
    
    mainImg_dwt = pywt.dwt2(main_image_gray_array, 'haar')
    LL, (LH, HL, HH) = mainImg_dwt

    # Alpha blending extract algorithm
    water_mark_coeficient_LL = (wLL - k*LL) /q

    extracted_watermark_dwt = water_mark_coeficient_LL, (wLH, wHL, wHH)

    # Inverse dwt algorith
    extracted_watermark = pywt.idwt2(extracted_watermark_dwt, 'haar')
    
    return Image.fromarray(extracted_watermark)


# ===============================================================
# Actual code below

# Images should be same lenght and height
# This divides full rgba numpy arrays
def addWaterMark(mainImg, markImg, k=k_g, q=q_g):
    #if img.mode != 'RGB':
    #    img.convert('RGB')
    
    #split image andwatermark into rgb arrays
    b, g, r = cv2.split(mainImg)
    m_b, m_g, m_r = cv2.split(markImg)
    
    #embed image to all above seperately
    #r
    w_r = embedMarkToArray(r, m_r)
    #g
    w_g = embedMarkToArray(g, m_g)
    #b
    w_b = embedMarkToArray(b, m_b)
    
    watermarked_image = cv2.merge((w_r,w_g,w_b))
    return watermarked_image

# Give RGBA arrays for this to process seperately
# This method embeds and do stuff to a seperate rgba numpy array
def embedMarkToArray(img_array, mark_array, k=k_g, q=q_g):
   
    main_image_dwt = pywt.dwt2(img_array, 'haar')
    LL, (LH, HL, HH) = main_image_dwt

    mark_image_dwt = pywt.dwt2(mark_array, 'haar')
    mLL, (mLH, mHL, mHH) = mark_image_dwt

    # Alpha Blend
    marked_LL = k*(LL) + q*(mLL)

    marked_dwt = marked_LL, (LH, HL, HH)
    water_marked_img = pywt.idwt2(marked_dwt, 'haar')

    return water_marked_img


# Images should be same lenght and height
# This uses rgb
def extractWatermark(mainImg, waterMarkedImg, k=k_g, q=q_g):
    
    #split image andwatermark into rgb arrays
    b, g, r = cv2.split(mainImg)
    #m_b, m_g, m_r = cv2.split(waterMarkedImg)
    m_r, m_g, m_b = cv2.split(waterMarkedImg)
    
    #extract image to all above seperately
    #r
    w_r = extractSeparateArray(r, m_r)
    #g
    w_g = extractSeparateArray(g, m_g)
    #b
    w_b = extractSeparateArray(b, m_b)
    
    water_mark = cv2.merge((w_r,w_g,w_b))
    return water_mark

# Give RGBA arrays for this to process seperately
# This method extracts and do stuff to a seperate rgb numpy array
def extractSeparateArray(main_image_array, water_marked_image_array, k=k_g, q=q_g):
   
    # dwt algorith
    waterMarkedImg_dwt = pywt.dwt2(water_marked_image_array, 'haar')
    wLL, (wLH, wHL, wHH) = waterMarkedImg_dwt
    
    mainImg_dwt = pywt.dwt2(main_image_array, 'haar')
    LL, (LH, HL, HH) = mainImg_dwt

    # Alpha blending extract algorithm
    water_mark_coeficient_LL = (wLL - k*LL) /q

    extracted_watermark_dwt = water_mark_coeficient_LL, (wLH, wHL, wHH)

    # Inverse dwt algorith
    extracted_watermark_array = pywt.idwt2(extracted_watermark_dwt, 'haar')
    return extracted_watermark_array