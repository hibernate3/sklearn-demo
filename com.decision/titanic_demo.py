import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.feature_extraction import DictVectorizer

if __name__ == '__main__':
    #获取数据
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

    # 决策树预估器
    estimator = DecisionTreeClassifier(criterion='entropy', max_depth=8)
    estimator.fit(x_train, y_train)

    # 模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict: \n', y_predict)
    print('直接比对真实值和预测值: \n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率为: \n', score)

    # 可视化决策树
    export_graphviz(estimator, out_file='titanic_tree.dot', feature_names=transfer.get_feature_names())

    # http://www.webgraphviz.com/ 生成可视化树

    pass

