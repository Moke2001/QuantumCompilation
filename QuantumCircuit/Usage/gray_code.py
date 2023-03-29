"""
函数：将Givens矩阵的Gray Code输出
gray_code(n, i, j)  --->  [code_vector,w_0]
code_vector：系列Gray_Code
w_0：目标qubit的量子位
"""

from Tool.BaseGate import *
from Tool.Binary import *


def gray_code(n:int, i_0:int, j_0:int):

    ## 准备工作
    global w_0
    i_bin = Binary(i_0, int(np.log2(n)))  # 基矢|i>的对应二进制串
    j_bin = Binary(j_0, int(np.log2(n)))  # 基矢|j>的对应二进制串
    code_vector = []  # 用于保存输出的Gray Code
    num = 0  # 用于循环计数

    ## 首先判断两个基矢之间差了多少个二进制位
    for k in range(i_bin.n):
        if i_bin.vec[k] != j_bin.vec[k]:
            num = num + 1  # 如果某一位上不同则num加1
        num_0=num

    ## 如果基矢之间不为一个相差位，那么进行SWAP化
    if num > 1:
        code_vector.append([i_bin.vec.copy(), -1])  # 先将起始的二进制串保留

        ## 调整较小的基矢
        for k in range(i_bin.n):
            if i_bin.vec[i_bin.n-1-k] != j_bin.vec[i_bin.n-1-k]:
                i_bin.change(i_bin.n-1-k)
                code_vector.append([i_bin.vec.copy(), k])
                num = num - 1

            ## 如果只剩下一个相差位，那么就停止
            if num == 1:

                ## 寻找余下的那个目标位
                for w in range(k, i_bin.n):
                    if i_bin.vec[w] != j_bin.vec[w]:  # w就是旋转对应的量子比特
                        w_0=w
                        break  #跳出循环

                break  # 跳出循环
    else:
        for w in range(i_bin.n):
            if i_bin.vec[w] != j_bin.vec[w]:  # w就是旋转对应的量子比特
                w_0 = w
                break  # 跳出循环

    return [code_vector,w_0]  # 返回得到的Gray Code序列


## 用于测试结果
if __name__=="__main__":
    [g,w_test]=gray_code(givens_test.shape[0], 0, 3)
    for i in range(len(g)):
        print(g[i][0])
