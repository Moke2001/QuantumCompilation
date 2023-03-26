###-------------------- 将一个多位受控U门分解 --------------------###
## 输入一个受控U门，将它分解为若干C^nNOT门，或者CZ门的序列
from QuantumCircuit.Tool.hermite import *


def cnu_decompose(cu_vector, U):  # cu_vector表示了各个位置的地位，U是作用的效果

    ## 1是控制位，2是目标位，-1是无关位
    moment=cu_vector.copy()
    num=0  # 控制位的个数
    for i in range(len(cu_vector)):
        if cu_vector[i]==0:
            num=num+1

    V=to_hermite(U)  # 将作用效果表示为矩阵V
    result=[]  # 结果储存在result里面
    for i in range(len(cu_vector)):  # 寻找目标位
        if moment[i]==2:
            for j in range(len(cu_vector)):  # 寻找某个控制位
                if moment[j]==1:
                    result.append(['cu',[[j,i],V.copy()]])  # 第一个量子门是一个受控U门
                    moment[j]=-1
                    result.append(['cnnot',moment])  # 第二个量子门是一个少一阶的CNNOT门
                    result.append(['cu',[[j,i],V.conjugate().transpose()]])  # 第三个量子门是一个受控U门
                    result.append(['cnnot',moment])  # 第四个量子门是一个少一阶的CNNOT门
                    num=num-1
                    if num==1:
                        result.append(['cu',[[j,i],V.copy()]])  # 如果分解到只剩一个控制位，那么就是一个CU门
                        break
                    else:
                        V = to_hermite(V)  # 否则的话对C^n-V门继续分解
            break
    return result
