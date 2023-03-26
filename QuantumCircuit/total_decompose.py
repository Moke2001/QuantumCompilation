###-------------------- 将一个量子门分解 --------------------###
## 输入一个矩阵，将它分解为若干RX,RY,RZ和CZ门的序列
from QuantumCircuit.GivensDecompose.givens_decompose import *
from QuantumCircuit.HighDecompose.qrd_decompose import *


def total_decompose(gate):
    [givens_vector,gate_0]=qrd_decompose(gate)
    result=[]
    for i in range(len(givens_vector)):
        [givens, [i, j]]=givens_vector[i]
        result=result+givens_decompose(givens, i, j)