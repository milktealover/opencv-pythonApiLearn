# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


def custom_blur_demo(image):  # �Զ���ģ��//07-1 �Զ���ģ��
    # kernel = np.ones([5, 5], np.float32) / 25
    # kernel = np.array([[1, 1, 1, 1], [1, 1, 1, 1], [ 1, 1, 1, 1], [ 1, 1, 1, 1]], np.float32) / 16  # �Զ����ֵ
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # �񻯣�����ο�����ɫ�ʾ��ģ��
    dst = cv.filter2D(image, -1, kernel)
    # cv.imshow("custom_blur_demo", dst)


def video_demo():  # ���ڵ��ô�����ͷ
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        custom_blur_demo(frame)
        cv.imshow("image", frame)
        if cv.waitKey(10) == 27:  # ��������q�˳����ڣ�����q����رջ�һֱ�ز��� Ҳ�������ó��������� & 0xFF == ord('q')
            break


# def video_play():# ��ȡ��Ƶ�ļ�
#     capture = cv.VideoCapture('12345.mp4')  # ��ȡ��Ƶ�ļ�
#     fps = capture.get(cv.CAP_PROP_FPS)  # ��ȡ����
#     size = (int(capture.get(cv.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv.CAP_PROP_FRAME_HEIGHT)))  # ��ȡ�ߴ�
#     fNUMS = capture.get(cv.CAP_PROP_FRAME_COUNT)  # ��ȡ֡��
#     cv.namedWindow("video", 0)
#     cv.resizeWindow("video", int(capture.get(cv.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv.CAP_PROP_FRAME_HEIGHT)))  # ���ò��Ŵ��ڳ��Ϳ�
#      #ret, frame = capture.read()  # ��ȡ��һ֡
#     while True:
#         ret, frame = capture.read()  # ��ȡ��һ֡
#         cv.imshow("video", frame)  # ��ʾĿǰ֡
#         cv.waitKey(5)  # �����ӳ٣����ڹۿ�����
#         # if cv.waitKey(10) & 0xFF == ord('q'):
#         #     break
#         if cv.waitKey(5) == 27:
#             break
#         ret, frame = capture.read()  # ��ȡ��һ֡
#     capture.release()


video_demo()
# video_play()
cv.destroyAllWindows()
