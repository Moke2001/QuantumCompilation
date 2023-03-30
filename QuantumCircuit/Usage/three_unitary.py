"""
函数：将一个单量子比特门拆解成三个量子门用于受控U门
three_unitary(U:某个单量子门,num:量子门作用位置)  --->  [A,B,C]
A,B,C：相应的三个量子门
"""

from QuantumCircuit.BaseDecompose.single_decompose import *


def three_unitary(U, target,control):

    ## 将相应的参数提取出来
    [beta,theta,alpha,delta]=single_decompose(U, target)
    delta = delta[1][1]
    alpha = alpha[1][1]
    theta = theta[1][1]
    beta = beta[1][1]

    ## 将参数赋值给A,B,C
    A=[['RY', [target, theta / 2]], ['RZ', [target, alpha]]]
    B=[['RZ', [target, (-beta - alpha) / 2]], ['RY', [target, -theta / 2]]]
    C=[['RZ', [target, (-alpha + beta) / 2]]]
    E=[['RZ',[control,delta+(alpha+beta)/2]]]

    return [A,B,C,E]  # 返回结果


## 用于测试结果
if __name__ == '__main__':
    [A_test,B_test,C_test,E_test] = three_unitary(H,0,1)  # 输出结果
    print([A_test,B_test,C_test])  # 打印结果
    output_operator(C_test+[['X',[0]]]+B_test+[['X',[0]]]+A_test,1)
