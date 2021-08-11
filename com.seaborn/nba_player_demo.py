import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def relation():
    '''
    相关性分析
    :return:
    '''
    print(data.describe())

    data_cor = data.loc[:,
               ['RPM', 'AGE', 'SALARY_MILLIONS', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'POINTS', 'GP',
                'MPG', 'ORPM', 'DRPM']]

    corr = data_cor.corr()

    plt.figure(figsize=(20, 8), dpi=100)
    sns.heatmap(corr, square=True, linewidths=0.1, annot=True)
    plt.show()


def base():
    # 薪资最高的10名运动员
    data.loc[:, ['PLAYER', 'RPM', 'AGE', 'SALARY_MILLIONS']].sort_values(by='SALARY_MILLIONS', ascending=False)

    # 效率值最高的10名运动员
    data.loc[:, ['PLAYER', 'RPM', 'AGE', 'SALARY_MILLIONS', 'MPG']].sort_values(by='RPM', ascending=False)


def single_distribution():
    '''
    单变量分布
    球员薪水、效率值、年龄这三个信息的分布情况
    :return:
    '''
    sns.set_style('darkgrid')
    plt.figure(figsize=(12, 12))

    plt.subplot(3, 1, 1)
    sns.distplot(data['SALARY_MILLIONS'])
    plt.xticks(np.linspace(0, 40, 9))
    plt.ylabel('Salary', size=10)

    plt.subplot(3, 1, 2)
    sns.distplot(data['RPM'])
    plt.xticks(np.linspace(-10, 10, 9))
    plt.ylabel('RPM', size=10)

    plt.subplot(3, 1, 3)
    sns.distplot(data['AGE'])
    plt.xticks(np.linspace(20, 40, 11))
    plt.ylabel('AGE', size=10)


def double_distribution():
    '''
    双变量分布
    年龄和薪水之间的关系
    :return:
    '''
    dat1 = data.loc[:, ['RPM', 'AGE', 'SALARY_MILLIONS', 'POINTS']]
    sns.jointplot(dat1.AGE, dat1.SALARY_MILLIONS, kind='hex', height=8)
    plt.show()


def multi_distribution():
    '''
    多变量分布
    多个变量之间的关系
    :return:
    '''
    dat1 = data.loc[:, ['RPM', 'AGE', 'SALARY_MILLIONS', 'POINTS']]
    sns.pairplot(dat1)
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv('nba_2017_nba_players_with_salary.csv')

    # single_distribution()
    # double_distribution()
    multi_distribution()

