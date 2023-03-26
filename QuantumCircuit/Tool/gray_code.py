###-------------------- Givens的Gray Code分解 --------------------###
# GrayCode输入参数为一个Givens矩阵，输出为一系列的Gray Code
from Tool.BaseGate import *
from Tool.Binary import *


def gray_code(n, i, j):  # givens是Givens矩阵，i、j都是矩阵中相互旋转的基矢

    global w_0
    i_bin = Binary(i, int(np.log2(n)))  # 基矢|i>的对应二进制串
    j_bin = Binary(j, int(np.log2(n)))  # 基矢|j>的对应二进制串
    code_vector = []  # 用于保存输出的Gray Code
    num = 0  # 用于循环计数

    ## 首先判断两个基矢之间差了多少个二进制位
    for k in range(i_bin.n):
        if i_bin.vec[k] != j_bin.vec[k]:
            num = num + 1  # 如果某一位上不同则num加1
        num_0=num
    ## 如果基矢之间不为一个相差位，那么进行SWAP化
    if num > 1:
        code_vector.append([i_bin.vec.copy(), -1])
        for k in range(i_bin.n):
            if i_bin.vec[k] != j_bin.vec[k]:
                i_bin.change(k)
                code_vector.append([i_bin.vec.copy(), k])
                num = num - 1
            if num == 1:
                for w in range(k, i_bin.n):
                    if i_bin.vec[w] != j_bin.vec[w]:  # w就是旋转对应的量子比特
                        w_0=w
                        break
                break
    return [code_vector,w_0]  # 返回得到的Gray Code序列


if __name__=="__main__":
    [g,w_0]=gray_code(givens_test, 0, 3)
    for i in range(len(g)):
        print(g[i][0])
