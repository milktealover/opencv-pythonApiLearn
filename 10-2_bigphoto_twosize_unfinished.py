import cv2 as cv
import numpy as np


def big_image_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row + ch, col:col + cw]
            hx = np.std(roi)
            if hx < 15:
                gray[row:row + ch, col:col + cw] = 255
            else:
                dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 4)
                # ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
                gray[row:row + ch, col:col + cw] = dst
                print(np.std(dst), np.mean(dst))
    cv.imwrite("D:\ophotos/resalt.png", gray)


src = cv.imread("D:\ophotos\out1.png")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
big_image_binary(src)
cv.waitKey(0)
cv.destroyAllWindows()
