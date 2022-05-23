import numpy as np
import cv2
import pywt
from PIL import Image

# Images should be same lenght and height
# This only uses grascale not full rgba
def embedWatermarkGrayScale(mainImg, markImg, k=0.85, q=0.009):
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
def extractWatermarkGrayScale(mainImg, waterMarkedImg, k=0.85, q=0.009):
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
def addWaterMark(mainImg, markImg, k=0.85, q=0.009):
    b, g, r = cv2.split(image)
    main_image_gray_array = np.mean(mainImg, -1)
    return k

# Give RGBA arrays for this to process seperately
# This method embeds and do stuff to a seperate rgba numpy array
def embedMarkToArray(img_array_part, markImg, k=0.85, q=0.009):
    main_image_gray_array = np.mean(mainImg, -1)
    return k