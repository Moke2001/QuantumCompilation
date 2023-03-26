###-------------------- 分解广义C^n-U门 --------------------###
## 将一个广义C^n-U门完全分解
from QuantumCircuit.GivensDecompose.cnnot_decompose import *


def general_cnnot(cnot_vector):  # cnot_vector表示了各个位置的地位，U是作用的效果

    ## 1是is控制位，2是目标位，-1是无关位，0是not控制位
    result=[]
    moment=cnot_vector.copy()
    for i in range(len(cnot_vector)):
        if moment[i]==0:
            result.append(['X',i])
            moment[i]=1
    result=result+cnnot_decompose(moment)
    for i in range(len(cnot_vector)):
        if cnot_vector[i]==0:
            result.append(['X',i])
    return result
