
#opencvとnumpyのimport
import cv2
import numpy as np

def binary(img):
    
    #グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    #閾値の設定
    threshold_value = 100

    #配列の作成（output用）
    threshold_img = gray.copy()

    #実装(numpy)
    threshold_img[gray < threshold_value] = 0
    threshold_img[gray >= threshold_value] = 255

    return threshold_img


if __name__ == "__main__":
    binary("image/sample.jpg")
    
