import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl


def cross_table():
    '''
    交叉表实现
    :return:
    '''
    # 数据加载
    data = pd.read_csv('stock_day.csv')

    # 数据处理
    time = pd.to_datetime(data.index)
    data['week'] = time.weekday
    data['p_n'] = np.where(data['p_change'] > 0, 1, 0)

    count = pd.crosstab(data['week'], data['p_n'])
    sum = count.sum(axis=1).astype(np.float32)
    ret = count.div(sum, axis=0)

    ret.plot(kind='bar', stacked=True)
    plt.show()


def pivot_table():
    '''
    透视表实现
    :return:
    '''
    # 数据加载
    data = pd.read_csv('stock_day.csv')

    # 数据处理
    time = pd.to_datetime(data.index)
    data['week'] = time.weekday
    data['p_n'] = np.where(data['p_change'] > 0, 1, 0)

    print(data.pivot_table(['p_n'], index='week'))



if __name__ == '__main__':
    # 设置显示中文字体
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    # 设置正常显示符号
    mpl.rcParams['axes.unicode_minus'] = False

    # cross_table()
    pivot_table()



