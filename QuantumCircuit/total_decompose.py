"""
函数：将一个量子门分解到通用量子门上
total_decompose(gate:某个量子门)  --->  result
result：分解结果，是量子门的序列
"""

from QuantumCircuit.GivensDecompose.givens_decompose import *
from QuantumCircuit.HighDecompose.qrd_decompose import *


def total_decompose(gate):

    ## 准备工作
    [givens_vector,gate_0]=qrd_decompose(gate)  # 将量子门的Givens矩阵找到
    result=[]  # 存储结果

    ## 分解每一个Givens矩阵
    for i in range(len(givens_vector)):
        [givens, [i, j]]=givens_vector[i]
        result=result+givens_decompose(givens, i, j)

    return result  # 输出分解的结果


## 用于测试结果
if __name__ == '__main__':
    result_test = total_decompose(Test)  # 输出结果
    print(result_test)
    output_operator(result_test,2)