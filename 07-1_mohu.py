# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


def blur_demo(image):  # ��ֵģ��
    dst = cv.blur(image, (10, 5))  # (x,y)   xΪˮƽ����,yΪ��ֱ����
    cv.imshow("blur_demo", dst)


def median_blur_demo(image):  # ��ֵģ��
    dst = cv.medianBlur(image, 5)  # ksizeΪ����
    cv.imshow("medianBlur", dst)


def custom_blur_demo(image):  # �Զ���ģ��
    # kernel = np.ones([5, 5], np.float32) / 25
    # kernel = np.array([[1, 1, 1, 1], [1, 1, 1, 1], [ 1, 1, 1, 1], [ 1, 1, 1, 1]], np.float32) / 16  # �Զ����ֵ
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # �񻯣�����ο�����ɫ�ʾ��ģ��
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
