# p7
import cv2 as cv
import numpy as np


def logic_demo_and(m1, m2):  # 逻辑与
    dst = cv.bitwise_and(m1, m2)
    cv.imshow("and", dst)


def logic_demo_or(m1, m2):  # 逻辑或
    dst = cv.bitwise_or(m1, m2)
    cv.imshow("or", dst)


def logic_demo_not(m1):  # 逻辑非
    dst = cv.bitwise_not(m1)
    cv.imshow("not", dst)


def logic_demo_xor(m1, m2):  # 逻辑异或
    dst = cv.bitwise_xor(m1, m2)
    cv.imshow("xor", dst)


def contrast_lightness_demo(image, c, b):  # c代表对比度,b代表亮度 ## 提升图片对比度与亮度
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1 - c, b)
    cv.imshow("lightness", dst)


src1 = cv.imread("D:\ophotos\linux.jpg")
src2 = cv.imread("D:\ophotos\win.jpg")
src = cv.imread("D:\ophotos\out.png")
# cv.imshow("image1", src1)
# cv.imshow("image2", src2)
cv.imshow("image", src)
logic_demo_and(src1, src2)
logic_demo_not(src1)
logic_demo_or(src1, src2)
logic_demo_xor(src1, src2)
contrast_lightness_demo(src, 0.2, 1)
cv.waitKey(0)
cv.destroyAllWindows()
