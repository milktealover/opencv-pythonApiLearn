import cv2 as cv
import numpy as np


def threshold_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 155, 255, cv.THRESH_TRUNC)  # 手册P22——p24
    print("ret={}".format(ret))
    cv.imshow("binary", binary)


def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 3)  # 手册P24——p25
    cv.imshow("binary", binary)


def custom_threshold(image):  # 均值二值化 ，mean 即是求出的均值
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w * h])
    mean = m.sum() / (w * h)
    print("mean={}".format(mean))
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.imshow("binary", binary)


src = cv.imread("D:\ophotos/QQ.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
#custom_threshold(src)
local_threshold(src)
cv.waitKey(0)
cv.destroyAllWindows()
