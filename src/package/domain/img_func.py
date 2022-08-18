import numpy as np
import cv2
import pywt
from PIL import Image

from src.package.utils.constants import ALPHA_BLEND_DEFAULT_K,ALPHA_BLEND_DEFAULT_Q

# Image  functions for embeding and extraction

def get_watermarked_img_with_info(main_image_gray_array, mark_image_gray_array, k=ALPHA_BLEND_DEFAULT_K, q=ALPHA_BLEND_DEFAULT_Q, n=1):
    main_image_dwt = pywt.dwt2(main_image_gray_array, 'haar')
    LL, (LH, HL, HH) = main_image_dwt
    mark_image_dwt = pywt.dwt2(mark_image_gray_array, 'haar')
    mLL, (mLH, mHL, mHH) = mark_image_dwt
    # Apla Blend
    marked_LL = k*(LL) + q*(mLL)
    marked_dwt = marked_LL, (LH, HL, HH)
    water_marked_img_array = pywt.idwt2(marked_dwt, 'haar')
    info = {}
    info['main_image_dwt'] = main_image_dwt
    info['mark_image_dwt'] = mark_image_dwt
    info['marked_LL'] = marked_LL
    info['water_marked_img_array'] = water_marked_img_array
    return info


def get_extracted_mark_with_info(main_image_gray_array,water_marked_image_gray_array, k=ALPHA_BLEND_DEFAULT_K, q=ALPHA_BLEND_DEFAULT_Q, n=1):
    # use => np.array(water_marked_img) , if the watermarked image is not an array
    # dwt algorithm
    water_marked_img_dwt = pywt.dwt2(water_marked_image_gray_array, 'haar')
    wLL, (wLH, wHL, wHH) = water_marked_img_dwt
    main_img_dwt = pywt.dwt2(main_image_gray_array, 'haar')
    LL, (LH, HL, HH) = main_img_dwt
    # Alpha blending extract algorithm
    water_mark_coeficient_LL = (wLL - k*LL) /q
    extracted_watermark_dwt = water_mark_coeficient_LL, (wLH, wHL, wHH)
    # Inverse dwt algorith
    extracted_watermark_array = pywt.idwt2(extracted_watermark_dwt, 'haar')
    info = {}
    info['water_marked_img_dwt'] = water_marked_img_dwt
    info['main_img_dwt'] = main_img_dwt
    info['water_mark_coeficient_LL'] = water_mark_coeficient_LL
    info['extracted_watermark_array'] = extracted_watermark_array
    return info


