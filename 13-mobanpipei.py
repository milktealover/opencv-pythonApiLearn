import cv2 as cv
import numpy as np


def contrast_lightness_demo(image, c, b):  # c代表对比度,b代表亮度 ## 提升图片对比度与亮度
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1 - c, b)
    return dst


def temple_demo(image1, image2):  # image2用于黑块
    # simple = cv.imread("D:\ophotos\in.png")
    # target = cv.imread("D:\ophotos\out.png")
    # cv.imshow("simple", simple)
    # cv.imshow("target", target)
    md = cv.TM_CCORR_NORMED
    wid, hei = image2.shape[:2]
    result = cv.matchTemplate(image1, image2, md)
    min_var, max_var, min_loc, max_loc = cv.minMaxLoc(result)
    tl = max_loc
    tl = (tl[0] + 10, tl[1] + 50)
    br = (tl[0] + hei, tl[1] + wid)
    cv.rectangle(image1, tl, br, [0, 0, 255], 3)
    return image1
    # cv.imshow("demo" + np.str(md), result)


def video_play():  # 读取视频文件
    capture = cv.VideoCapture('D:\ophotos\donttouchwithe.mp4')  # 读取视频文件
    fps = capture.get(cv.CAP_PROP_FPS)  # 获取码率
    # size = (int(capture.get(cv.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv.CAP_PROP_FRAME_HEIGHT)))  # 获取尺寸
    # fNUMS = capture.get(cv.CAP_PROP_FRAME_COUNT)  # 获取帧数
    # cv.namedWindow("video",0)
    # cv.resizeWindow("video", int(capture.get(cv.CAP_PROP_FRAME_WIDTH)),
    #                 int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))-900)  # 设置播放窗口长和宽
    # ret, frame = capture.read()  # 读取第一帧
    img1 = cv.imread("D:\ophotos/black.png")
    while True:
        ret, frame = capture.read()  # 读取下一帧
        frame = contrast_lightness_demo(frame, 0.5, 100)
        frame = temple_demo(frame, img1)
        frame = contrast_lightness_demo(frame, 0.8, 0.01)
        cv.imshow("video", frame)  # 显示目前帧
        #   cv.waitKey(5)  # 设置延迟，便于观看体验
        # if cv.waitKey(10) & 0xFF == ord('q'):
        #     break
        if cv.waitKey(5) == 27:
            break
        ret, frame = capture.read()  # 读取下一帧
    capture.release()


# src = cv.imread("D:\ophotos\out.png")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
# temple_demo()
video_play()
cv.waitKey(0)
cv.destroyAllWindows()
