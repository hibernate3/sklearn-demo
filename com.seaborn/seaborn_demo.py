import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def func1():
    '''
    绘制单变量分布
    :return:
    '''
    np.random.seed(0)
    arr = np.random.randn(100)
    print(arr)

    # 绘制直方图
    ax = sns.distplot(arr, bins=10, hist=True, kde=True, rug=True)
    plt.show()


if __name__ == '__main__':
    func1()
    pass

