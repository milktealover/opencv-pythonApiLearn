import cv2 as cv
import numpy as np


def bi_demo(image):  # 高斯双边模糊
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("demo", dst)


def shift_demo(image):  # 均值迁移模糊
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow("shift_demo", dst)


src = cv.imread("D:\ophotos\exm1.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
bi_demo(src)
shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
