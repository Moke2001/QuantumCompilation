###-------------------- 将一个Givens矩阵分解 --------------------###
## 输入一个Givens矩阵，将它分解为若干Toffoli门，CZ门和单量子门的序列
# QR的输入参数为一个n*n的矩阵，输出为一系列的Givens矩阵
from QuantumCircuit.GivensDecompose.general_cnnot import *
from QuantumCircuit.GivensDecompose.general_cnu import *
from QuantumCircuit.Tool.gray_code import *


def givens_decompose(givens,i,j):

    n=givens.shape[0]
    [code_vector,target]=gray_code(n,i,j)
    U=np.array([[givens[i][i],givens[i][j]],[givens[j][i],givens[j][j]]])  # 作用效果矩阵
    result=[]

    for i in range(len(code_vector)):
        [moment,invert]=code_vector[i]
        if i==len(code_vector)-1:
            moment[target] = 2
            result = result + general_cnu(moment, U)
        else:
            moment[invert] = 2
            result = result + general_cnnot(moment)

    for i in range(len(code_vector)-1):
        result=result+result[len(code_vector)-2-i]

    return result


