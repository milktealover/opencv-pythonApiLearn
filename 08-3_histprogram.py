import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def back_projection_demo():
    simple = cv.imread("D:\ophotos\simple1.png")
    target = cv.imread("D:\ophotos/target1.png")
    simple_hsv = cv.cvtColor(simple, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)
    cv.imshow("simple_demo", simple)
    cv.imshow("target_demo", target)
    sim_hist = cv.calcHist([simple_hsv], [0, 1], None, [2, 2], [0, 180, 0, 256])
    cv.normalize(sim_hist, sim_hist, 0, 255, cv.NORM_MINMAX)
    # cv.normalize() 使用博客
    # https://blog.csdn.net/cosmispower/article/details/64457406?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522163549193016780262513844%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=163549193016780262513844&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-64457406.first_rank_v2_pc_rank_v29&utm_term=cv.normalize&spm=1018.2226.3001.4187
    hsv = cv.calcBackProject([target_hsv], [0, 1], sim_hist, [0, 180, 0, 256], 1)
    '''
    void cv::calcBackProject    (   const Mat *     images,
        int     nimages,
        const int *     channels,
        InputArray      hist,
        OutputArray     backProject,
        const float **      ranges,
        double      scale = 1,
        bool    uniform = true 
    )
    参数解释：
    const Mat* images:输入图像，图像深度必须位CV_8U,CV_16U或CV_32F中的一种，尺寸相同，每一幅图像都可以有任意的通道数
    int nimages:输入图像的数量
    const int* channels:用于计算反向投影的通道列表，通道数必须与直方图维度相匹配，第一个数组的通道是从0到image[0].channels()-1,第二个数组通道从图像image[0].channels()到image[0].channels()+image[1].channels()-1计数
    InputArray hist:输入的直方图，直方图的bin可以是密集(dense)或稀疏(sparse)
    OutputArray backProject:目标反向投影输出图像，是一个单通道图像，与原图像有相同的尺寸和深度
    const float ranges**:直方图中每个维度bin的取值范围
    double scale=1:可选输出反向投影的比例因子
    bool uniform=true:直方图是否均匀分布(uniform)的标识符，有默认值true
    '''
    hsv1 = cv.bitwise_or(target, 255, None, hsv)
    cv.imshow("hsv", hsv1)


def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0, 1], None, [180, 256], [0, 180, 0, 256])
    # calcHist()使用博客
    # https://blog.csdn.net/keith_bb/article/details/56680997?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522163549240616780255223400%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=163549240616780255223400&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-56680997.first_rank_v2_pc_rank_v29&utm_term=cv.calcHist&spm=1018.2226.3001.4187
    # cv.imshow("hist2d", hist)
    plt.imshow(hist, interpolation="nearest")
    plt.title("hist2d")
    plt.show()


# src = cv.imread("D:\ophotos\exm1.png")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
# hist2d_demo(src)
back_projection_demo()
cv.waitKey(0)
cv.destroyAllWindows()
