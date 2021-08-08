import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris


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


def func2():
    '''
    绘制双变量分布——散点图
    :return:
    '''
    # 创建DataFrame对象
    dataframe_obj = pd.DataFrame({"x": np.random.randn(500), "y": np.random.randn(500)})

    # 绘制散布图
    sns.jointplot(x="x", y="y", data=dataframe_obj, kind='scatter', color='r', size=8, ratio=5, space=0.2)
    plt.show()


def func3():
    '''
    绘制双变量分布——直方图
    :return:
    '''
    # 创建DataFrame对象
    dataframe_obj = pd.DataFrame({"x": np.random.randn(500), "y": np.random.randn(500)})

    # 绘制散布图
    sns.jointplot(x="x", y="y", data=dataframe_obj, kind='hex')
    plt.show()


def func4():
    '''
    绘制双变量分布——直方图
    :return:
    '''
    # 创建DataFrame对象
    dataframe_obj = pd.DataFrame({"x": np.random.randn(500), "y": np.random.randn(500)})

    # 绘制散布图
    sns.jointplot(x="x", y="y", data=dataframe_obj, kind='kde')
    plt.show()


def func5():
    '''
    绘制成对的双变量分布
    :return:
    '''
    iris = pd.read_csv('iris.csv')

    # 绘制多个成对的双变量分布
    sns.pairplot(iris)
    plt.show()


def func6():
    '''
    绘制类别散点图
    :return:
    '''
    tips = pd.read_csv('tips.csv')

    # 方式一：数据点会有重叠
    sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='time')

    # 方式二：数据点都不会重叠
    # sns.swarmplot(x="day", y="total_bill", data=tips, hue='time')
    plt.show()


def func7():
    '''
    绘制箱型图
    :return:
    '''
    tips = pd.read_csv('tips.csv')
    # sns.boxplot(x='day', y='total_bill', data=tips, hue='time')
    sns.boxplot(x='day', y='total_bill', data=tips)
    plt.show()


def func8():
    '''
    绘制提琴图
    :return:
    '''
    tips = pd.read_csv('tips.csv')
    sns.violinplot(x="day", y="total_bill", data=tips)
    plt.show()


def func9():
    '''
    类别内得估计统计——绘制条形图
    :return:
    '''
    tips = pd.read_csv('tips.csv')
    sns.barplot(x="day", y="total_bill", data=tips)
    plt.show()


def func10():
    '''
    类别内得估计统计——绘制条形图
    :return:
    '''
    tips = pd.read_csv('tips.csv')
    sns.pointplot(x="day", y="total_bill", data=tips)
    plt.show()


if __name__ == '__main__':
    func10()
    pass

