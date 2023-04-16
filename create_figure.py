import numpy as np
import cv2 as cv


def line_demo():  # 生成直线
    # Create a black image
    img = np.zeros((512, 512, 3), np.uint8)
    # Draw a diagonal blue line with thickness of 5 px
    cv.line(img, (0, 0), (511, 511), (0, 255, 0), 5)  # 起点，终点，图像色彩(蓝，绿，红)，宽度
    cv.imshow("line", img)


def rectangle_demo():  # 生成矩形
    # Create a black image
    img = np.zeros((512, 512, 3), np.uint8)
    cv.rectangle(img, (10, 10), (50,500), (125, 0, 125), 3)  # 左上顶点，右下顶点，图像色彩(蓝，绿，红)，宽度
    cv.imshow("rectangle", img)


line_demo()
rectangle_demo()
cv.waitKey(0)
cv.destroyAllWindows()
