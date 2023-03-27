"""
函数：将CNU门完全分解
cnnot_decompose(cu_vector:表征地位的数组)  --->  result
result：分解结果，是一个通用门序列
"""

from QuantumCircuit.GivensDecompose.cnnot_decompose import *
from QuantumCircuit.Usage.hermite import *


def cnu_decompose(cu_vector, U):  # cu_vector表示了各个位置的地位，U是作用的效果

    ## 1是控制位，2是目标位，-1是无关位
    moment=cu_vector.copy()
    num=0  # 控制位的个数
    for i in range(len(cu_vector)):
        if cu_vector[i]==0:
            num=num+1
    V=to_hermite(U)  # 将作用效果表示为矩阵V
    result=[]  # 结果储存在result里面

    ## 第一层循环，寻找目标位
    for target in range(len(cu_vector)):
        if moment[target]==2:

            ## 第二层循环，寻找控制位
            for control in range(len(cu_vector)):
                if moment[control]==1:

                    ## 将线路分解
                    result=result+cu_decompose(V.copy(),control,target) # 第一个量子门是一个受控U门
                    result=result+cnnot_decompose(moment)  # 第二个量子门是一个少一阶的CNNOT门
                    result=result+cu_decompose(V.conjugate().transpose().copy(),control,target)  # 第三个量子门是一个受控U门
                    result=result+cnnot_decompose(moment)  # 第四个量子门是一个少一阶的CNNOT门
                    num=num-1  # 控制位减少1
                    moment[control] = -1  # 控制位变无关位

                    ## 如果减少一个控制位后为CU门，则直接给出
                    if num==1:
                        result=result+cu_decompose(V.copy(),control,target)  # 如果分解到只剩一个控制位，那么就是一个CU门
                        break

                    ## 否则继续寻找下一个控制位，对C^n-V门继续分解
                    else:
                        V = to_hermite(V)

            break  # 跳出循环

    return result  # 返回结果


## 用于测试结果
if __name__ == '__main__':
    result_test = cnu_decompose([1,-1,1,2,1],H)  # 输出结果
    print(result_test)  # 打印结果
    output_operator(result_test,5)
