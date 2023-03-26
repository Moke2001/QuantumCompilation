from Tool.BaseGate import *


def to_hermite(U):
    eigenvalues, eigenvectors = np.linalg.eig(U)  # 对 N 进行特征分解
    V = eigenvectors
    Lambda = np.diag(eigenvalues)
    sqrt_Lambda = np.sqrt(Lambda)  # 对 Lambda 取平方根
    return V @ sqrt_Lambda @ np.linalg.inv(V)  # 输出结果


if __name__ == "__main__":
    W=to_hermite(Test)
    N=W@W
    a=N-Test
    x=1+1
