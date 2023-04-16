# p6
import cv2 as cv
import numpy as np


def add_photo(m1, m2):  # 图片数据加法
    dst = cv.add(m1, m2)
    cv.imshow("add_photo", dst)


def subtract_photo(m1, m2):  # 图片数据减法
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_photo", dst)


def divide_photo(m1, m2):  # 图片数据除法
    dst = cv.divide(m1, m2)
    cv.imshow("divide_photo", dst)


def multiply_photo(m1, m2):  # 图片数据乘法
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_photo", dst)


def others(m1, m2):  # 对图像数据求均值
    # M1 = cv.mean(m1)      # 求平均值
    M1, dev1 = cv.meanStdDev(m1)  # 求平均值以及方差
    M2, dev2 = cv.meanStdDev(m2)
    print("M1:", M1, "\n", M2)
    print("dev:", dev1, "\n", dev2)
    h, w = m1.shape[:2]
    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m, dev)


src1 = cv.imread("D:\ophotos\linux.jpg")
src2 = cv.imread("D:\ophotos\win.jpg")
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
cv.namedWindow("image2", cv.WINDOW_AUTOSIZE)
print(src1.shape)
print(src2.shape)
cv.imshow("image1", src1)
cv.imshow("image2", src2)
add_photo(src1, src2)
subtract_photo(src1, src2)
divide_photo(src1, src2)
multiply_photo(src1, src2)
others(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()
