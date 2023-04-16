import cv2 as cv
import numpy as np


def create_image():
    img = np.zeros([400, 400, 3], np.uint8)  # blue green red
    img[:, :, 0] = np.ones([400, 400]) * 255
    cv.imshow("new image", img)
    cv.waitKey(500)
    img[:, :, 1] = np.ones([400, 400]) * 255
    cv.imshow("new image", img)
    cv.waitKey(500)
    img[:, :, 2] = np.ones([400, 400]) * 255
    cv.imshow("new image", img)
    img = np.zeros([400, 400, 1], np.uint8)
    img[:, :, 0] = np.ones([400, 400]) * 127
    cv.imshow("new image", img)
    cv.waitKey(500)
    m1 = np.ones([3, 3], np.float32)
    m1.fill(122.3456)
    print(m1)
    m2 = m1.reshape([1, 9])
    print(m2)
    m3 = np.array([[1,2,3],[3,4,5],[5,6,7]],np.uint32)
    m3.fill(255)
    print(m3)


create_image()
cv.waitKey(0)
