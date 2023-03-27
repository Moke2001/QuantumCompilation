"""
函数：用QRD算法分解量子门，得到一系列Givens矩阵
qrd_decompose(gate:某个矩阵)  --->  [gate_vector,gate_0]
gate_vector=[Givens矩阵,[i,j]]  (i<j)
gate_0：分解的结果，用于验证分解成功
"""

from Tool.BaseGate import *
from Tool.Binary import *
import matplotlib.pyplot as plt


def qrd_decompose(gate: np.array):

    ## 准备工作
    n = gate.shape[0]  # 量子门维度
    gate_0 = gate  # 保存初始量子门的状态
    gate_vector = []  # 分解得到的Givens矩阵按乘积顺序放在该数组里

    ## 从最左下方开始分解，从下到上，从左到右，分解到对角线为止
    for i in range(n - 1):  # 列循环，从左到右
        for j in range(n - i - 1):  # 行循环，从下到上

            ## 初始化矩阵G，使得它是一个单位矩阵
            G = np.zeros((n, n), dtype=complex)
            for k in range(n):
                G[k][k] = 1

            ## 将循环变量转换为置位变量
            j_0 = n - j - 1  # Givens矩阵的作用元1
            k_0 = j_0 - 1  # Givens矩阵的作用元2
            i_0 = i  # 矩阵元将消失的列数
            model = np.sqrt(np.abs(gate_0[j_0][i_0]) ** 2 + np.abs(gate_0[k_0][i_0]) ** 2)  # 计算用的模长

            ## 如果一个位置上已经近似为0，那么跳过该元
            if np.abs(gate_0[j_0][i_0]) <= 0.0001:  # 设定精确度
                gate_vector.insert(0, [G, [-1, -1]])
                continue

            ## 将计算得到的Givens矩阵的矩阵元大小赋予相应位次
            G[k_0][k_0] = np.conj(gate_0[k_0][i_0]) / model
            G[k_0][j_0] = np.conj(gate_0[j_0][i_0]) / model
            G[j_0][k_0] = -gate_0[j_0][i_0] / model
            G[j_0][j_0] = gate_0[k_0][i_0] / model

            gate_0 = G @ gate_0 # 经过一个Givens矩阵变换后的矩阵

            ## 设定返回格式，确保i<j
            if k_0 > j_0:
                gate_vector.append([np.linalg.inv(G), [j_0, k_0]])
            else:
                gate_vector.append([np.linalg.inv(G), [k_0, j_0]])

    return [gate_vector, gate_0]  # 返回分解的结果


## 用于测试结果
if __name__ == '__main__':

    [gate_vector_test, gate_test] = qrd_decompose(Test)  # 输出结果

    ## 将表格可视化输出
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('off')
    tb = ax.table(cellText=gate_test.tolist(), loc='center')
    tb.auto_set_font_size(False)
    tb.set_fontsize(8)
    plt.show()
