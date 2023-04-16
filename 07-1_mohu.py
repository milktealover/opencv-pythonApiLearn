# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


def blur_demo(image):  # 均值模糊
    dst = cv.blur(image, (10, 5))  # (x,y)   x为水平方向,y为竖直方向
    cv.imshow("blur_demo", dst)


def median_blur_demo(image):  # 中值模糊
    dst = cv.medianBlur(image, 5)  # ksize为奇数
    cv.imshow("medianBlur", dst)


def custom_blur_demo(image):  # 自定义模糊
    # kernel = np.ones([5, 5], np.float32) / 25
    # kernel = np.array([[1, 1, 1, 1], [1, 1, 1, 1], [ 1, 1, 1, 1], [ 1, 1, 1, 1]], np.float32) / 16  # 自定义均值
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 锐化，更多参考常用色彩卷积模板
    dst = cv.filter2D(image, -1, kernel)
    cv.imshow("custom_blur_demo", dst)


src = cv.imread("D:\ophotos\chou.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
blur_demo(src)
median_blur_demo(src)
custom_blur_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
