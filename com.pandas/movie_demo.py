import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl


def base_info():
    '''
    基本信息获取
    :return:
    '''
    print('电影平均分', movie['Rating'].mean())
    print('导演总人数', np.unique(movie['Director']).shape[0])


def rating_show():
    '''
    分数分布
    :return:
    '''
    plt.figure(figsize=(20, 8), dpi=80)
    plt.hist(movie["Rating"].values, bins=20)

    # 求出最大最小值
    max_ = movie["Rating"].max()
    min_ = movie["Rating"].min()

    # 生成刻度列表
    t1 = np.linspace(min_, max_, num=21)

    # 修改刻度
    plt.xticks(t1)

    # 添加网格
    plt.grid()
    plt.show()


def runtime_show():
    '''
    runting分布
    :return:
    '''
    plt.figure(figsize=(20, 8), dpi=80)
    plt.hist(movie["Runtime (Minutes)"].values, bins=20)

    # 求出最大最小值
    max_ = movie["Runtime (Minutes)"].max()
    min_ = movie["Runtime (Minutes)"].min()

    # 生成刻度列表
    t1 = np.linspace(min_, max_, num=21)

    # 修改刻度
    plt.xticks(t1)
    # 添加网格
    plt.grid()
    plt.show()


def genre_show():
    # 进行字符串分割
    temp_list = [i.split(',') for i in movie['Genre']]
    # 获取电影的分类
    genre_list = np.unique([i for j in temp_list for i in j])
    # 增加新的列
    temp_df = pd.DataFrame(np.zeros([movie.shape[0], genre_list.shape[0]]), columns=genre_list)

    for i in range(1000):
        temp_df.ix[i, temp_list[i]] = 1
    print(temp_df.sum().sort_values())

    temp_df.sum().sort_values(ascending=False).plot(kind='bar', figsize=(20, 8), fontsize=20, colormap='cool')
    plt.show()


if __name__ == '__main__':
    # 设置显示中文字体
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    # 设置正常显示符号
    mpl.rcParams['axes.unicode_minus'] = False

    movie = pd.read_csv('IMDB-Movie-Data.csv')

    # base_info()
    # rating_show()
    # runtime_show()
    pass

