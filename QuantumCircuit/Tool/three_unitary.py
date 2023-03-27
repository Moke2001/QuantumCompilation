"""
函数：将一个单量子比特门拆解成三个量子门用于受控U门
three_unitary(U:某个单量子门,num:量子门作用位置)  --->  [A,B,C]
A,B,C：相应的三个量子门
"""

from QuantumCircuit.BaseDecompose.single_decompose import *


def three_unitary(U,num):

    ## 将相应的参数提取出来
    [beta,theta,alpha,delta]=single_decompose(U,num)
    delta = delta[1][1]
    alpha = alpha[1][1]
    theta = theta[1][1]
    beta = beta[1][1]

    ## 将参数赋值给A,B,C
    A=[['RZ',[num,beta]],['RY',[num,theta/2]]]
    B=[['RY',[num,-theta/2]],['RZ',[num,(-beta-alpha) / 2]]]
    C=[['RZ', [num,(alpha-beta) / 2]]]
    D=[['I', [num,delta]]]

    return [A,B,C,D]  # 返回结果


## 用于测试结果
if __name__ == '__main__':
    [A_test,B_test,C_test,D_test] = three_unitary(H,0)  # 输出结果
    print([A_test,B_test,C_test])  # 打印结果
    main(A_test+[['X', [0]]]+B_test+[['X', [0]]]+C_test+D_test)