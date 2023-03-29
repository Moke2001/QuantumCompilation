"""
函数：将CNNOT门完全分解
cnnot_decompose(cnot_vector:表征地位的数组)  --->  result
result：分解结果，是一个通用门序列
"""

from QuantumCircuit.BaseDecompose.toffoli_decompose import *


def cnnot_decompose(cnot_vector):  # cu_vector表示了各个位置的地位

    ## 1是控制位，2是目标位，-1是无关位
    V = 1 / (1 + 1j) * np.array([[1, 1j], [1j, 1]])  # 控制门
    moment = cnot_vector.copy()  # 复制地位向量
    num = 0  # 控制位的个数
    result = []  # 结果储存在result里面
    i_vector=[]

    ## 计算控制位的个数
    for i in range(len(cnot_vector)):
        if cnot_vector[i] == 1:
            num = num + 1
            i_vector.append(i)
        elif cnot_vector[i]==2:
            target_pre=i

    if num == 1:
        result=[['CX',[i_vector[0],target_pre]]]
    elif num==2:
        result=toffoli_decompose(i_vector[0],i_vector[1],target_pre)
    else:
        ## 第一层循环寻找目标位，找到就break
        for target in range(len(cnot_vector)):
            if moment[target] == 2:

                ## 第二层循环寻找控制位，找到也break
                for control in range(len(cnot_vector)):
                    if moment[control] == 1:

                        ## 递归处理
                        moment[control] = -1  # 将moment控制位设置为无关位
                        num = num - 1  # 因此控制位个数少了一个

                        ## 递归出口
                        if num == 2:

                            ## 找到下一个控制位
                            for k in range(control, len(cnot_vector)):
                                if moment[k] == 1:
                                    result = cu_decompose(V,control,target) + toffoli_decompose(control, k, target) + cu_decompose(V.conj().T,control,target) + toffoli_decompose(control, k, target)

                        ## 递归体
                        else:
                            result = cu_decompose(V,target,control) + cnnot_decompose(moment.copy()) + cu_decompose(V.conj().T,control,target) + cnnot_decompose(moment.copy())

                    break  # 找到控制位就break

                break  # 找到目标位就break

    return result  # 返回结果


## 用于测试结果
if __name__ == '__main__':
    result_test = cnnot_decompose([1,-1,1,2,1])  # 输出结果
    print(result_test)  # 打印结果
    output_operator(result_test,5)

