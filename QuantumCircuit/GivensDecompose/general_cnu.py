"""
函数：将一个广义CNU门完全分解
general_cnu(cnu_vector, U)  --->  result
result：量子门序列
"""

from QuantumCircuit.GivensDecompose.cnu_decompose import *


def general_cnu(cnu_vector, U):

    ## 1是is控制位，2是目标位，-1是无关位，0是not控制位
    result=[]
    moment=cnu_vector.copy()

    ## 寻找0控制位
    for i in range(len(cnu_vector)):
        if cnu_vector[i]==0:
            result.append(['X',[i]])
            moment[i]=1

    result=result+cnu_decompose(moment,U)  ## 作用一般的CNU门

    ## 将X反写在0控制位qubits上
    for i in range(len(cnu_vector)):
        if cnu_vector[i]==0:
            result.append(['X',[i]])

    return result  # 返回结果


## 用于测试结果
if __name__=="__main__":
    result_test=general_cnu([1,0,2,-1],H)
    print(result_test)
    output_operator(result_test,4)

