import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    weight = image.shape[1]
    channels = image.shape[2]
    print("height:{}\tweight:{}\tchannels:{}".format(height, weight, channels))
    for hei in range(height):  # 遍历所有像素点，对所有像素点执行操作
        for wei in range(weight):
            for cha in range(channels):
                pv = image[hei, wei, cha]
                image[hei, wei, cha] = 255 - pv
    cv.imshow("pixels", image)


def inverst(image):
    rst = cv.bitwise_not(image)     # 实现access_pixels()这个函数的功能，即对图像数据取反
    cv.imshow("inverst demo", rst)


src = cv.imread("D://ophotos//out3.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
t1 = cv.getTickCount()  # 获取CPU当前时钟总数
access_pixels(src)
# inverst(src)
t2 = cv.getTickCount()
print("time:{} ms".format((t2 - t1) / cv.getTickFrequency() * 1000))
cv.waitKey(0)
cv.destroyAllWindows()
