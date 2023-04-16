import cv2 as cv
import numpy as np



def lapalian_demo(image):
    # dst = cv.Laplacian(image, cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)
    kernel = np.array([[1, 0, 1], [0, -4, 0], [1, 0, 1]])
    dst = cv.filter2D(image, cv.CV_32F, kernel=kernel)
    # dst = cv.Laplacian(image,cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lpls", lpls)


def sobel_demo(image):
    # grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    # grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("x", gradx)
    cv.imshow("y", grady)
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("jihe", gradxy)


src = cv.imread("D:\ophotos/target.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# lapalian_demo(src)
sobel_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
