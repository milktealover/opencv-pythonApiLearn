import cv2 as cv
import numpy as np


def extract_object_demo():
    caputer = cv.VideoCapture("D:/opencv_study/12345.mp4")
    while (True):
        ret, frame = caputer.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_RGB2HSV)
        cv.imshow("vedio", frame)
        lower_hsv = np.array([37, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lower_hsv, upper_hsv)
        dst = cv.bitwise_and(frame,frame, mask=255-mask)
        cv.imshow("mask", dst)
        c = cv.waitKey(40)
        if c == 27:
            break


# src = cv.imread("D:\ophotos\out.png")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
extract_object_demo()
cv.waitKey(0)
cv.destroyAllWindows()
