import cv2 as cv
import numpy as np


def clame(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


def gossizaoshen(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)  # 建议了解，不太清楚
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            image[row, col, 0] = clame(b + s[0])
            image[row, col, 1] = clame(g + s[1])
            image[row, col, 2] = clame(r + s[2])
            cv.imshow("noise_image", image)


src = cv.imread("D:\ophotos\chou.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
t1 = cv.getTickCount()
gossizaoshen(src)
t2 = cv.getTickCount()
time = (t2 - t1) / cv.getTickFrequency()
print(time)
dst = cv.GaussianBlur(src, (5, 5), 0)  # 此函数为高斯模糊函数
cv.imshow("gaussblur", dst)  # 结果证明高斯模糊可对高斯噪声进行降噪
cv.waitKey(0)
cv.destroyAllWindows()
