"""
函数：将一个单量子比特门完全分解
single_decompose(U:某个单量子门,num:量子门作用位置)  --->  result
result：量子门序列
"""

from Tool.BaseGate import *
from QiskitInterface.operator import *


def single_decompose(U,num):

    ## 将量子门元素记录下来
    a = U[0][0];c = U[1][0]
    a1 = np.real(U[0][0]) ; a2 = np.imag(U[0][0])
    b1 = np.real(U[0][1]) ; b2 = np.imag(U[0][1])
    c1 = np.real(U[1][0]) ; c2 = np.imag(U[1][0])
    d1 = np.real(U[1][1]) ; d2 = np.imag(U[1][1])

    ## 如果第一个元素为0
    if a == 0:
        theta = 0
        delta = (np.arcsin(c2) - np.arcsin(b2)) / 2
        alpha = 0
        beta = (-np.arcsin(c2) - np.arcsin(b2)) / 2

    ## 如果第三个元素为0
    elif c == 0:
        theta = np.pi
        delta = (np.arcsin(a2) + np.arcsin(d2)) / 2
        alpha = 0
        beta = np.arcsin(d2) - np.arcsin(a2)

    ## 正常情况
    else:
        theta = 2 * np.arctan(np.abs(a) / np.abs(c))
        alpha = np.arcsin(c2) - np.arcsin(a2)
        beta = np.arcsin(b2) - np.arcsin(a2) - np.pi
        delta = 0.5 * (-np.arcsin(b2) + np.arcsin(c2) - np.pi)

    return [['RZ',[num,beta]],['RY',[num,theta]],['RZ',[num,alpha]],['I',[num,delta]]]  # 返回分解的结果


## 用于测试结果
if __name__ == '__main__':
    result_test = single_decompose(H,0)  # 输出结果
    print(result_test)  # 打印结果
    output_operator(result_test,1)