import matplotlib.pyplot as plt
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score


if __name__ == '__main__':
    # 创建数据集
    # X为样本特征，Y为样本簇类别， 共1000个样本，每个样本2个特征，共4个簇，
    # 簇中⼼在[-1,-1], [0,0],[1,1], [2,2]， 簇⽅差分别为[0.4, 0.2, 0.2, 0.2]
    x, y = make_blobs(n_samples=1000, n_features=2, centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],
                      cluster_std=[0.4, 0.2, 0.2, 0.2], random_state=9)
    # 数据集可视化
    plt.scatter(x[:, 0], x[:, 1], marker='o')
    plt.show()

    # 使⽤k-means进⾏聚类,并使⽤CH⽅法评估
    y_pred = KMeans(n_clusters=2, random_state=9).fit_predict(x)
    # 分别尝试n_cluses=2\3\4,然后查看聚类效果
    plt.scatter(x[:, 0], x[:, 1], c=y_pred)
    plt.show()
    # ⽤Calinski-Harabasz Index评估的聚类分数
    print(calinski_harabasz_score(x, y_pred))
    pass

