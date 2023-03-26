###-------------------- 将一个受控U门分解 --------------------###
## 输入一个U，将它分解为A，B，C
from QuantumCircuit.BaseDecompose.single_decompose import *


def three_unitary(U):
    [delta,alpha, theta,beta]=single_decompose(U)
    delta=delta[1]
    alpha = alpha[1]
    theta = theta[1]
    beta = beta[1]
    A=[['RZ',alpha],['RY',theta/2]]
    B=[['RY',-theta/2],['RZ',(-beta-alpha) / 2]]
    C=[['RZ', (beta-alpha) / 2]]
    return [A,B,C]
