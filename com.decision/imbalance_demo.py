from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
from collections import Counter
from imblearn.over_sampling import RandomOverSampler
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler


if __name__ == '__main__':
    # 准备类别不平衡数据
    x, y = make_classification(n_samples=5000,
                               n_features=2,  # 特征个数
                               n_informative=2,  # 多信息的特征个数
                               n_redundant=0,  # 冗余信息
                               n_repeated=0,  # 重复信息
                               n_classes=3,  # 分类类别
                               n_clusters_per_class=1,  # 某一个类别是由几个cluster构成的
                               weights=[0.01, 0.05, 0.94],  # 列表类型，权重比
                               random_state=0)

    print(Counter(y))

    # 数据可视化
    plt.scatter(x[:, 0], x[:, 1], c=y)
    plt.show()

    # 使用imblearn进行随机过采样
    ros = RandomOverSampler(random_state=0)
    x_resampled, y_resampled = ros.fit_resample(x, y)
    print(Counter(y_resampled))
    plt.scatter(x_resampled[:, 0], x_resampled[:, 1], c=y_resampled)
    plt.show()

    # SMOTE过采样
    x_resampled, y_resampled = SMOTE().fit_resample(x, y)
    print(Counter(y_resampled))
    plt.scatter(x_resampled[:, 0], x_resampled[:, 1], c=y_resampled)
    plt.show()

    # 欠采样
    rus = RandomUnderSampler(random_state=0)
    x_resampled, y_resampled = rus.fit_resample(x, y)
    print(Counter(y_resampled))
    plt.scatter(x_resampled[:, 0], x_resampled[:, 1], c=y_resampled)
    plt.show()



