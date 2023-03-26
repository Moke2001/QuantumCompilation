###-------------------- 将一个C^n-NOT门分解 --------------------###
## 将一个C^n-NOT门完全分解
from QuantumCircuit.BaseDecompose.toffoli_decompose import *


def cnnot_decompose(cu_vector):  # cu_vector表示了各个位置的地位

    ## 1是控制位，2是目标位，-1是无关位
    V = 1 / (1 + 1j) * np.array([1, 1j], [1j, 1])  # 控制门
    moment = cu_vector.copy()
    num = 0  # 控制位的个数

    for i in range(len(cu_vector)):
        if cu_vector[i] == 0:
            num = num + 1

    result = []  # 结果储存在result里面
    for i in range(len(cu_vector)):  # 寻找目标位
        if moment[i] == 2:
            for j in range(len(cu_vector)):  # 寻找某个控制位
                if moment[j] == 1:
                    moment[j] = -1
                    num = num - 1
                    if num == 2:
                        for k in range(j, len(cu_vector)):
                            if moment[k] == 1:
                                result = cu_decompose([[j, i], V]) + toffoli_decompose(j, k, i) + cu_decompose(
                                    [[j, i], V.conj().T]) + toffoli_decompose(j, k, i)
                    else:
                        result = cu_decompose([[j, i], V]) + cnnot_decompose(moment.copy()) + cu_decompose(
                            [[j, i], V.conj().T]) + cnnot_decompose(moment.copy())
                break
            break

    return result
