import cv2 as cv
import numpy as np


def temple_demo():
    simple = cv.imread("D:\ophotos\in.png")
    target = cv.imread("D:\ophotos\out.png")
    cv.imshow("simple", simple)
    cv.imshow("target", target)
    method = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    wid, hei = simple.shape[:2]
    for md in method:
        result = cv.matchTemplate(target, simple, md)
        min_var, max_var, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0] + hei, tl[1] + wid)
        cv.rectangle(target, tl, br, [0, 0, 255], 1)
        cv.imshow("demo" + np.str(md), target)
        # cv.imshow("demo" + np.str(md), result)


# src = cv.imread("D:\ophotos\out.png")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
temple_demo()
cv.waitKey(0)
cv.destroyAllWindows()
