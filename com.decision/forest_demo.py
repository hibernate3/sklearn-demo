from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import pandas as pd

if __name__ == '__main__':
    '''
    随机森林对泰坦尼克号乘客的生存进行预测
    '''
    # 获取数据
    path = 'http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt'
    titanic = pd.read_csv(path)

    # 筛选特征值和目标值
    x = titanic['pclass', 'age', 'sex']
    y = titanic['survived']

    # 数据处理
    # 缺失值处理
    x['age'].fillna(x['age'].mean(), inplace=True)

    # 转换成字典
    x.to_dict(orient='records')

    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22)

    # 字典特征抽取
    transfer = DictVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    #  随机森林预估器
    estimator = RandomForestClassifier()

    # 加入网格搜索与交叉验证
    param_dict = {'n_estimators': [120, 200, 300, 500, 800, 1200],
                  'max_depth': [5, 8, 15, 25, 30]}
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

