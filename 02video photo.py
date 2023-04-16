# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


def custom_blur_demo(image):  # 自定义模糊//07-1 自定义模糊
    # kernel = np.ones([5, 5], np.float32) / 25
    # kernel = np.array([[1, 1, 1, 1], [1, 1, 1, 1], [ 1, 1, 1, 1], [ 1, 1, 1, 1]], np.float32) / 16  # 自定义均值
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 锐化，更多参考常用色彩卷积模板
    dst = cv.filter2D(image, -1, kernel)
    # cv.imshow("custom_blur_demo", dst)


def video_demo():  # 用于调用打开摄像头
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        custom_blur_demo(frame)
        cv.imshow("image", frame)
        if cv.waitKey(10) == 27:  # 键盘输入q退出窗口，不按q点击关闭会一直关不掉 也可以设置成其他键。 & 0xFF == ord('q')
            break


# def video_play():# 读取视频文件
#     capture = cv.VideoCapture('12345.mp4')  # 读取视频文件
#     fps = capture.get(cv.CAP_PROP_FPS)  # 获取码率
#     size = (int(capture.get(cv.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv.CAP_PROP_FRAME_HEIGHT)))  # 获取尺寸
#     fNUMS = capture.get(cv.CAP_PROP_FRAME_COUNT)  # 获取帧数
#     cv.namedWindow("video", 0)
#     cv.resizeWindow("video", int(capture.get(cv.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv.CAP_PROP_FRAME_HEIGHT)))  # 设置播放窗口长和宽
#      #ret, frame = capture.read()  # 读取第一帧
#     while True:
#         ret, frame = capture.read()  # 读取下一帧
#         cv.imshow("video", frame)  # 显示目前帧
#         cv.waitKey(5)  # 设置延迟，便于观看体验
#         # if cv.waitKey(10) & 0xFF == ord('q'):
#         #     break
#         if cv.waitKey(5) == 27:
#             break
#         ret, frame = capture.read()  # 读取下一帧
#     capture.release()


video_demo()
# video_play()
cv.destroyAllWindows()
