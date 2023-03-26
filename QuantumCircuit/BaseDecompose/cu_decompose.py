###-------------------- 将一个受控U门分解 --------------------###
## 输入一个受控U门，将它分解为若干CNOT门，或者CZ门的序列
from QuantumCircuit.BaseDecompose.single_decompose import *
from QuantumCircuit.Tool.three_unitary import *


def cu_decompose(cu):
    [[j,i],U]=cu  # j是控制位，i是目标位，U是作用效果
    [A,B,C]=three_unitary(U)  # 将门分解为A,B,C三个门
    result= A+[['CX', [j, i]]]+B+['CX', [j, i]]+C
    return result



