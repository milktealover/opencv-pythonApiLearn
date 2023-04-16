import cv2 as cv
import numpy as np


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pr_data = np.array(image)
    print(pr_data)


src = cv.imread("D:\ophotos\out.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
get_image_info(src)
cv.imwrite("D:\ophotos\out1.png", src)
src = cv.cvtColor(src, cv.COLOR_HSV2BGR)
cv.namedWindow("out",cv.WINDOW_AUTOSIZE)
cv.imshow("out",src)
cv.waitKey(0)
cv.destroyAllWindows()
