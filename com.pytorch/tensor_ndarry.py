from __future__ import print_function
import torch
import numpy as np


def tensor2Ndarray():
    # Torch Tensor和Numpy array共享底层的内存空间, 因此改变其中一个的值, 另一个也会随之被改变
    a = torch.ones(5)
    print(a)

    # 将Torch Tensor转换为Numpy array
    b = a.numpy()
    print(b)

    # 对其中一个进行加法操作, 另一个也随之被改变
    a.add_(1)
    print(a)
    print(b)


def ndarray2Tensor():
    a = np.ones(5)
    b = torch.from_numpy(a)
    np.add(a, 1, out=a)
    print(a)
    print(b)


def cpu2Gpu():
    x = torch.rand(5, 3)

    # 如果服务器上已经安装了GPU和CUDA
    if torch.cuda.is_available():
        # 定义一个设备对象, 这里指定成CUDA, 即使用GPU
        device = torch.device("cuda")
        # 直接在GPU上创建一个Tensor
        y = torch.ones_like(x, device=device)
        # 将在CPU上面的x张量移动到GPU上面
        x = x.to(device)
        # x和y都在GPU上面, 才能支持加法运算
        z = x + y
        # 此处的张量z在GPU上面
        print(z)
        # 也可以将z转移到CPU上面, 并同时指定张量元素的数据类型
        print(z.to("cpu", torch.double))
    else:
        print("fuck gpu")



if __name__ == '__main__':
    # tensor2Ndarray()
    # ndarray2Tensor()
    pass

