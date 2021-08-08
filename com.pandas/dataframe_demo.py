import pandas as pd
import numpy as np

if __name__ == '__main__':
    # 生成10名同学，5门功课的数据
    score = np.random.randint(40, 100, (10, 5))

    # 使用Pandas中的数据结构
    score_df = pd.DataFrame(score)

    # 构造行索引序列
    subjects = ["语文", "数学", "英语", "政治", "体育"]

    # 构造列索引序列
    stu = ['同学' + str(i) for i in range(score_df.shape[0])]

    # 添加行索引
    data = pd.DataFrame(score, columns=subjects, index=stu)

    # 修改索引值
    stu = ["学生_" + str(i) for i in range(score_df.shape[0])]
    # 必须整体全部修改
    data.index = stu

    print(data)
    pass


