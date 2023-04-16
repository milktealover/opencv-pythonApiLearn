# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


def equalHist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("last", gray)
    dst = cv.equalizeHist(gray)
    cv.imshow("equalHist_demo", dst)


def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("last", gray)
    clahe = cv.createCLAHE(clipLimit=2, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow("clahe_demo", dst)


def creat_rgb_hist(image):
    h, w, c = image.shape
    rgbhist = np.zeros([16 * 16 * 16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b / bsize) * 16 * 16 + np.int(g / bsize) * 16 + np.int(r / bsize)
            rgbhist[np.int(index), 0] = rgbhist[np.int(index), 0] + 1
    return rgbhist


def hist_compare(image1, image2):
    hist1 = creat_rgb_hist(image1)
    hist2 = creat_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴氏距离:%s;相关性:%s;卡方:%s." % (match1, match2, match3))


src = cv.imread("D:\ophotos\mei.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# equalHist_demo(src)
# clahe_demo(src)
src1 = cv.imread("D:\ophotos\outt2.png")
src2 = cv.imread("D:\ophotos\out.png")
cv.imshow("src1", src1)
cv.imshow("src2", src2)
hist_compare(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()
