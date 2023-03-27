"""
函数：将一个Toffoli门完全分解
toffoli_decompose(c_1:第一控制位,c_2:第二控制位,target:目标位)  --->  result
result：量子门序列
"""

from QuantumCircuit.BaseDecompose.cu_decompose import *


def toffoli_decompose(c_1:int,c_2:int,target:int):
    V=np.array([[1,1j],[1j,1]])/(1+1j)  # 张登玉构型的基本单门
    result = cu_decompose(V,c_2,target) + [['CX',[c_1,target]]] + cu_decompose(V.conj().T,c_2,target) +[['CX',[c_1,target]]]
    return result  # 返回结果


## 用于测试结果
if __name__=="__main__":
    result_test=toffoli_decompose(0,1,3)
    print(result_test)
    output_operator(result_test,4)