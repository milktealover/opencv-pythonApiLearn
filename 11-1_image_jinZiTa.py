import cv2 as cv
import numpy as np


def pyramid_demo(image):
    leval = 3
    temp = image.copy()
    pyraimd_images = []  # 创建了一个列表依次将每一次Down后的图像保存在里面
    for i in range(leval):
        dst = cv.pyrDown(temp)
        pyraimd_images.append(dst)
        cv.imshow("pyramid_demo" + str(i), dst)
        temp = dst.copy()
    return pyraimd_images


def lapulasi_demo(image):  # 拉普拉斯金字塔
    pyraimd_images = pyramid_demo(image)
    leval = len(pyraimd_images)
    for i in range(leval - 1, -1, -1):
        if (i - 1) < 0:
            expond = cv.pyrUp(pyraimd_images[i], dstsize=image.shape[:2])
            lsp = cv.subtract(image, expond)
            cv.imshow("lsp_demo" + str(i), lsp)
        else:
            expond = cv.pyrUp(pyraimd_images[i], dstsize=pyraimd_images[i - 1].shape[:2])
            lsp = cv.subtract(pyraimd_images[i - 1], expond)
            cv.imshow("lsp_demo" + str(i), lsp)


src = cv.imread("D:\ophotos\outto2.png")  # 对于拉普拉斯金字塔只可以用outto2.png,因为它的大小是特制的，是有要求的，必须为2的n次方*2的n次方;
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
pyramid_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
