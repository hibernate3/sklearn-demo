import pandas as pd
from sklearn.decomposition import PCA


if __name__ == '__main__':
    # 获取数据
    order_products = pd.read_csv('order_products__prior.csv')
    products = pd.read_csv('products.csv')
    orders = pd.read_csv('orders.csv')
    aisles = pd.read_csv('aisles.csv')

    # 合并表
    # 合并orders和order_products on=order_id tab1:order_id, product_id, user_id
    tab1 = pd.merge(orders, order_products, on=['order_id', 'order_id'])

    # 合并tab1和products
    tab2 = pd.merge(tab1, products, on=["product_id", "product_id"])

    # 合并tab2和aisles
    tab3 = pd.merge(tab2, aisles, on=["aisle_id", "aisle_id"])

    # 交叉表处理，把user_id和aisle进行分组，找到userid和aisle之间的关系
    table = pd.crosstab(tab3["user_id"], tab3["aisle"])

    # 主成分分析的方法进行降维
    transfer = PCA(n_components=0.95)

    data = transfer.fit_transform(table)

    print(data.shape)

    


