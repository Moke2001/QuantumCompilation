###-------------------- 分解广义C^n-U门 --------------------###
## 将一个广义C^n-U门完全分解
from QuantumCircuit.GivensDecompose.cnu_decompose import *


def general_cnu(cnu_vector, U):# cu_vector表示了各个位置的地位，U是作用的效果

    ## 1是is控制位，2是目标位，-1是无关位，0是not控制位
    result=[]
    moment=cnu_vector.copy()
    for i in range(len(cnu_vector)):
        if cnu_vector[i]==0:
            result.append(['X',i])
            moment[i]=1
    result=result+cnu_decompose(moment,U)
    for i in range(len(cnu_vector)):
        if cnu_vector[i]==0:
            result.append(['X',i])
    return result

