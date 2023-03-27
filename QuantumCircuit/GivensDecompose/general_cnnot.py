"""
函数：将一个广义CNNOT门完全分解
general_cnnot(cnot_vector, U)  --->  result
result：量子门序列
"""

from QuantumCircuit.GivensDecompose.cnnot_decompose import *


def general_cnnot(cnot_vector):

    ## 1是is控制位，2是目标位，-1是无关位，0是not控制位
    result=[]
    moment=cnot_vector.copy()

    ## 寻找0控制位
    for i in range(len(cnot_vector)):
        if moment[i]==0:
            result.append(['X',i])
            moment[i]=1

    result=result+cnnot_decompose(moment) ## 作用一般的CNNOT门

    ## 将X反写在0控制位qubits上
    for i in range(len(cnot_vector)):
        if cnot_vector[i]==0:
            result.append(['X',i])

    return result  # 返回结果


## 用于测试结果
if __name__=="__main__":
    result_test=general_cnnot([1,0,2,-1])
    print(result_test)
    output_operator(result_test,4)
