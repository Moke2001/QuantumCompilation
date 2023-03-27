"""
函数：将低维度的门延拓到高维度上
dimension_change(U:低维度门, n:, n_vector_in)  --->  matrix
V：U的平方因子
"""

from Tool.Binary import *
from Tool.BaseGate import *
import numpy as np


def dimension_change(U, n, n_vector_in):
    ## 准备工作
    n_0 = int(np.log2(U.shape[0]))  # 起始作用的qubits个数
    n_vector_out = []  # 存放输出的串向量
    count = 0  # 计数器
    i = 1  # 计数器

    ## 寻找不在原始门上的比特
    while 1:
        if n_vector_in[count] == i:
            if count != n_0 - 1:
                count = count + 1
        elif n_vector_in[count] > i and count != n_0 - 1:
            n_vector_out.append(i)
        elif n_vector_in[count] > i and count == n_0 - 1:
            n_vector_out.append(i)
        elif n_vector_in[count] < i and count == n_0 - 1:
            n_vector_out.append(i)
        elif n_vector_in[count] < i and count != n_0 - 1:
            count = count + 1
            i = i - 1
        i = i + 1
        if count == n_0 - 1 and i == n + 1:
            break

    ## 求高维度的门的形式
    matrix = np.zeros((2 ** n, 2 ** n), dtype='complex_')  # 初始化矩阵
    core = Binary(np.zeros(n), 0)  # 总量子比特的状态
    kernel_out = Binary(np.zeros(len(n_vector_out)), 0)  # 不在原始门中量子比特的状态

    ## 实现低维到高维的转化
    for w in range(2 ** n // 2 ** n_0):
        location = np.zeros(2 ** n_0)  # 计算一个系列各个所在的列
        moment = core.value  # 计算一个系列两个列的间隔
        kernel_in = Binary(np.zeros(len(n_vector_in)), 0)  # 在原始门中量子比特的状态
        for j in range(2 ** n_0):
            location[j] = moment
            kernel_in = kernel_in + Binary([1], 0)
            core_moment = Binary(core.vec.copy(), 0)
            for i in range(len(n_vector_in)):
                core.vec[n_vector_in[i] - 1] = kernel_in.vec[i]
            moment = moment + ((core - core_moment).to_decimal())
        for i in range(2 ** n_0):
            for j in range(2 ** n_0):
                matrix[int(location[i])][int(location[j])] = U[i][j]
        kernel_out = kernel_out + Binary([1], 0)
        for i in range(len(n_vector_out)):
            core.vec[n_vector_out[i] - 1] = kernel_out.vec[i]

    return matrix  # 返回延拓后的矩阵


## 用于测试结果
if __name__ == "__main__":
    matrix_test=dimension_change(CZ, 3, [0, 1])
    print(matrix_test)
