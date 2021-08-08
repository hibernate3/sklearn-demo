import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score

if __name__ == '__main__':
    '''
    逻辑回归对癌症进行预测
    '''

    # 读取数据，处理缺失值以及标准化
    column_name = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                   'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                   'Normal Nucleoli', 'Mitoses', 'Class']

    path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'
    data = pd.read_csv(path, names=column_name)

    # 缺失值处理
    data = data.replace(to_replace='?', value=np.nan)
    data.dropna(inplace=True)
    print(data.isnull().any())

    # 筛选特征值和目标值
    x = data.iloc[:, 1:-1]
    y = data['Class']

    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22)

    # 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 模型预估器
    estimator = LogisticRegression()
    estimator.fit(x_train, y_train)

    # 逻辑回归的模型参数：回归系数和偏置
    print('回归系数: \n', estimator.coef_)
    print('偏置: \n', estimator.intercept_)

    # 模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict: \n', y_predict)
    print('直接比对真实值和预测值: \n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率为: \n', score)

    # 查看准确率，召回率，F1-score
    report = classification_report(y_test, y_predict, labels=[2, 4], target_names=['良性', '恶性'])
    print(report)

    # 计算AUC指标
    # 将y_test转换为 0，1
    y_true = np.where(y_test > 3, 1, 0)
    auc = roc_auc_score(y_true, y_predict)
    print('AUC指标: \n', auc)

    pass

