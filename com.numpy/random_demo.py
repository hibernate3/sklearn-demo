import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl


def normal_distribution():
    '''
    正态分布
    :return:
    '''
    x1 = np.random.normal(1.75, 1, 1000000)

    # 生成均匀分布的随机数
    x1 = np.random.normal(1.75, 1, 100000000)
    # 画图看分布状况
    # 1）创建画布
    plt.figure(figsize=(20, 10), dpi=100)
    # 2）绘制直方图
    plt.hist(x1, 1000)
    # 3）显示图像
    plt.show()
    return None


def uniform_distribution():
    '''
    均匀分布
    :return:
    '''
    # 生成均匀分布的随机数
    x2 = np.random.uniform(-1, 1, 1000000)
    # 画图看分布状况
    # 1）创建画布
    plt.figure(figsize=(10, 10), dpi=100)
    # 2）绘制直方图
    plt.hist(x=x2, bins=1000)  # x代表要使用的数据，bins表示要划分区间数
    # 3）显示图像
    plt.show()
    return None


if __name__ == '__main__':
    # normal_distribution()
    uniform_distribution()
    pass

