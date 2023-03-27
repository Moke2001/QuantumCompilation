"""
函数：给出一个矩阵的平方因子
to_hermite(U:酉矩阵)  --->  V
V：U的平方因子
"""

from Tool.BaseGate import *


def to_hermite(U):

    eigenvalues, eigenvectors = np.linalg.eig(U)  # 对 N 进行特征分解
    V = eigenvectors  # 特征向量
    lambda_0 = np.diag(eigenvalues)  # 取特征值
    sqrt_Lambda = np.sqrt(lambda_0)  # 对 lambda 取平方根
    return V @ sqrt_Lambda @ np.linalg.inv(V)  # 输出结果


## 用于测试结果
if __name__ == "__main__":
    W=to_hermite(Test)  # 测试分解
    N=W@W  # 测试平方
    a=N-Test  #a=0说明函数没错
