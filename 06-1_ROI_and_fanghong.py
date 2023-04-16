import cv2 as cv
import numpy as np


def fill_color_demo(image):
    copyimage = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h + 2, w + 2], np.uint8)
    cv.floodFill(copyimage, mask, [30, 30], [0, 0, 0], [0, 100,0], [200, 200, 200],
                 cv.FLOODFILL_FIXED_RANGE)  # 1.操作的图像, 2.掩模, 3.起始像素值，4.填充的颜色, 5.填充颜色的低值， 6.填充颜色的高值 ,7.填充的方法)
    cv.imshow("fill_demo", copyimage)


src = cv.imread("D:\ophotos\out.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
fill_color_demo(src)
face = src[150:250, 305:389]
gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
back = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
src[150:250, 305:389] = back
cv.imshow("face", src)
cv.waitKey(0)
cv.destroyAllWindows()
