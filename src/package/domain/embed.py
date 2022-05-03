import numpy as np
import pywt

# Images should be same lenght and height
# This only uses grascale not full rgba
def embedWatermarkGrayScale(mainImg,markImg,k=0.85,q=0.009):
    main_image_gray_array = np.mean(mainImg, -1)
    mark_image_gray_array = np.mean(markImg, -1)
    
    main_image_dwt = pywt.dwt2(main_image_gray_array, 'haar')
    LL, (LH, HL, HH) = main_image_dwt

    mark_image_dwt = pywt.dwt2(mark_image_gray_array, 'haar')
    mLL, (mLH, mHL, mHH) = mark_image_dwt

    # Apla Blend
    marked_LL = k*(LL) +q*(mLL)

    marked_dwt = marked_LL, (LH, HL, HH)
    water_marked_img = pywt.idwt2(marked_dwt, 'haar')
    return water_marked_img

