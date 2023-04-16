import cv2 as cv

src = cv.imread("D:\ophotos\mei.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
b, g, r = cv.split(src)  # 拆
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)
src[:, :, 0] = 255
cv.imshow("changed image1", src)
src1 = cv.merge([b, g, r])  # 和
cv.imshow("changed image2", src1)
cv.waitKey(0)
cv.destroyAllWindows()
