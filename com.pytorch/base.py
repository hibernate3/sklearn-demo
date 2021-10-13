from __future__ import print_function
import torch

if __name__ == '__main__':
    # 创建一个没有初始化的矩阵
    x = torch.empty(5, 3)
    print(x)

    # 创建一个有初始化的矩阵
    x = torch.rand(5, 3)
    print(x)

    # 创建一个全零矩阵并可指定数据元素的类型为long
    x = torch.zeros(5, 3, dtype=torch.long)
    print(x)

    # 直接通过数据创建张量
    x = torch.tensor([2.5, 3.5])
    print(x)

    # 通过已有的一个张量创建相同尺寸的新张量
    # 利用news_methods方法得到一个张量
    x = x.new_ones(5, 3, dtype=torch.double)
    print(x)

    # 利用randn_like方法得到相同张量尺寸的一个新张量, 并且采用随机初始化来对其赋值
    y = torch.randn_like(x, dtype=torch.float)
    print(y)

    print(x.size())

    # 加法操作
    print(x + y)
    print(torch.add(x, y))

    # 加法操作：提前设定一个空的张量
    result = torch.empty(5, 3)
    # 将空的张量作为加法的结果存储张量
    torch.add(x, y, out=result)
    print(result)

    # 加法操作：原地置换
    y.add_(x)
    print(y)

    # 用类似于Numpy的方式对张量进行操作
    x = torch.randn(4, 4)
    print(x)
    print(x[:, 1])

    # 改变张量的形状
    x = torch.randn(4, 4)
    # tensor.view()操作需要保证数据元素的总数量不变
    y = x.view(16)
    # -1代表自动匹配个数
    z = x.view(-1, 8)
    print(x.size(), y.size(), z.size())

    # 如果张量中只有一个元素, 可以用.item()将值取出, 作为一个python number
    x = torch.randn(1)
    print(x)
    print(x.item())
    pass

