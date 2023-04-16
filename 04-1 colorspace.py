import cv2 as cv


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    cv.imshow("rgb", rgb)
    hsv = cv.cvtColor(image, cv.COLOR_RGB2HSV)
    cv.imshow("hsv", hsv)
    hls = cv.cvtColor(image, cv.COLOR_RGB2HLS)
    cv.imshow("hls", hls)
    ycrcb = cv.cvtColor(image, cv.COLOR_RGB2YCrCb)
    cv.imshow("ycrcb", ycrcb)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)


src = cv.imread("D:\ophotos\out3.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
color_space_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
