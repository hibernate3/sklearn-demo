import numpy as np
import pandas as pd

def func1():
    '''
    缺失值处理
    :return:
    '''
    # 读取电影数据
    movie = pd.read_csv("IMDB-Movie-Data.csv")

    # 判断缺失值是否存在
    print(pd.notnull(movie))
    print(np.all(pd.notnull(movie)))

    # 替换所有缺失值
    for i in movie.columns:
        if np.all(pd.notnull(movie[i])) == False:
            print(i)
            movie[i].fillna(movie[i].mean(), inplace=True)

    return None

if __name__ == '__main__':
    func1()
    pass

