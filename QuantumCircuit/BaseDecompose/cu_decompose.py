"""
函数：将一个CU门完全分解
cu_decompose(c_1:第一控制位,c_2:第二控制位,target:目标位)  --->  result
result：量子门序列
"""

from QuantumCircuit.Usage.three_unitary import *


def cu_decompose(U,control,target):  # control是控制位，target是目标位，U是作用效果
    [A,B,C,E]=three_unitary(U,target,control)  # 将门分解为A,B,C三个门
    result= C+[['CX', [control, target]]]+B+[['CX', [control, target]]]+A+E
    return result


## 用于测试结果
if __name__ == '__main__':
    ts=np.array([[1/np.sqrt(2),-1/np.sqrt(2)],[1/np.sqrt(2),1/np.sqrt(2)]])
    result_test = cu_decompose(ts,1,0)  # 输出结果
    print(result_test)
    output_operator(result_test,2)



