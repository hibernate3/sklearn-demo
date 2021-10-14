from __future__ import print_function
import torch


def base():
    x1 = torch.ones(3, 3)
    print(x1)

    x = torch.ones(2, 2, requires_grad=True)
    print(x)

    y = x + 2
    print(y)

    # 打印Tensor的grad_fn属性
    print(x.grad_fn)
    print(y.grad_fn)

    # 在Tensor上执行更复杂的操作
    z = y * y * 3
    out = z.mean()
    print(z, out)

    out.backward()
    print(x)
    print(x.grad)

    print(x.requires_grad)
    print((x ** 2).requires_grad)

    # 终止反向求导
    with torch.no_grad():
        print((x ** 2).requires_grad)

    print(x.requires_grad)
    y = x.detach()
    print(y.requires_grad)
    print(x.eq(y).all())
    pass


def advance():
    # 关于方法.requires_grad_(): 该方法可以原地改变Tensor的属性.requires_grad的值. 如果没有主动设定默认为False
    a = torch.randn(2, 2)
    a = ((a * 3) / (a - 1))
    print(a.requires_grad)
    a.requires_grad_(True)
    print(a.requires_grad)
    b = (a * a).sum()
    print(b.grad_fn)
    pass


if __name__ == '__main__':
    base()
    pass

