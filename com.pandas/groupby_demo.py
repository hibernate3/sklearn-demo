import numpy as np
import pandas as pd


if __name__ == '__main__':
    col = pd.DataFrame(
        {'color': ['white', 'red', 'green', 'red', 'green'], 'object': ['pen', 'pencil', 'pencil', 'ashtray', 'pen'],
         'price1': [5.56, 4.20, 1.30, 0.56, 2.75], 'price2': [4.75, 4.12, 1.60, 0.75, 3.15]})

    print(col, '\n')

    # 方式一
    print(col.groupby(['color'])['price1'].mean(), '\n')
    # 保留索引
    print(col.groupby(['color'], as_index=False)['price1'].mean(), '\n')

    # 方式二
    print(col['price1'].groupby(col['color']).mean())
    pass

