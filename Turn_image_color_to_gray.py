import cv2 as cv
import numpy as np

src = cv.imread("D:\ophotos/1.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.imwrite("D:\ophotos/1-1.png",gray)
cv.waitKey(0)
cv.destroyAllWindows()

