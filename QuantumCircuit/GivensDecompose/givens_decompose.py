"""
函数：将一个Givens矩阵完全分解为基本门序列
givens_decompose(givens:Givens矩阵,i:作用元数1,j:作用元数2)  --->  result
result：量子门序列
"""

from QuantumCircuit.GivensDecompose.general_cnnot import *
from QuantumCircuit.GivensDecompose.general_cnu import *
from QuantumCircuit.Usage.gray_code import *


def givens_decompose(givens:np.array,i_0:int,j_0:int):

    ## 准备工作
    n=givens.shape[0]  # Givens矩阵的维度数
    [code_vector,target]=gray_code(n,i_0,j_0)  # 给出两个作用元连接的Gray Code，调用了函数gray_code()
    U=np.array([[givens[i_0][i_0],givens[i_0][j_0]],[givens[j_0][i_0],givens[j_0][j_0]]])  # 作用效果矩阵，因此要求矩阵从小向大对齐
    result=[]  # 存储分解的门序列结果

    ## 处理Gray Code
    for k in range(len(code_vector)):

        ## U门作用前作用由Gray Code决定作用CNNOT门
        [moment,invert]=code_vector[k]
        if k==len(code_vector)-1:  # 如果分解到最后一个，那么用CNU门
            moment[target] = 2
            flag=len(result)  # 记录分解到了哪里
            result = result + general_cnu(moment, U)  ## 调用函数general_cnu()
        else:  # 没有分解到最后一个，那么用CNNOT门
            moment[invert] = 2
            result = result + general_cnnot(moment)  ## 调用函数general_cnnot()

    ## U门作用后将之前的CNNOT门反向
    if len(code_vector)>0:
        for w in range(flag):
            result.append(result[flag-w-1])  # 反向收集量子门

    return result  # 返回结果


## 用于测试结果
if __name__ == '__main__':
    result_test = givens_decompose(givens_test,1,3)  # 输出结果
    print(result_test,2)

