import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

if __name__ == '__main__':
    # 获取数据
    data = pd.read_csv('train.csv')

    # 基本的数据处理
    # 缩小数据范围
    data = data.query('x<2.5 & x>2 & y<1.5 & y>1.0')

    # 处理时间特征
    time_value = pd.to_datetime(data['time'], unit='s')
    date = pd.DatetimeIndex(time_value)
    data['day'] = date.day
    data['weekday'] = date.weekday
    data['hour'] = date.hour

    # 过滤签到次数少的地点
    place_count = data.groupby('place_id').count()['row_id']
    data_final = data[data['place_id'].isin(place_count[place_count > 3].index.values)]

    # 筛选目标值和特征值
    x = data_final[['x', 'y', 'accuracy', 'day', 'weekday', 'hour']]
    y = data_final['place_id']

    # 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    # 特征工程：标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # KNN算法预估器
    estimator = KNeighborsClassifier()

    # 加入网格搜索与交叉验证
    param_dict = {'n_neighbors': [3, 5, 7, 9]}
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=3)

    estimator.fit(x_train, y_train)

    # 模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict: \n', y_predict)
    print('直接比对真实值和预测值: \n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率为: \n', score)

    print('最佳参数: \n', estimator.best_params_)
    print('最佳结果: \n', estimator.best_score_)
    print('最佳估计器: \n', estimator.best_estimator_)
    print('交叉验证结果: \n', estimator.cv_results_)

    pass

