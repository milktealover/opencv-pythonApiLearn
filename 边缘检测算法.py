# -*- coding=GBK -*-
import cv2 as cv


# ��Ե������㷨
def edge_image(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)# �ȶ���ģ������������
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)# ���ض�ֵ��
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    cv.imshow("canny��Ե", edge_output)
    dst = cv.bitwise_and(image, image, mask=edge_output)
    cv.imshow("color��Ե", dst)


src = cv.imread("D:\ophotos\out.png")
cv.imshow("ԭ��", src)
edge_image(src)
cv.waitKey(0)
cv.destroyAllWindows()