###-------------------- QRD算法分解量子门 --------------------###
# QR的输入参数为一个n*n的矩阵，输出为一系列的Givens矩阵
from Tool.BaseGate import *
from Tool.Binary import *
import matplotlib.pyplot as plt


def qrd_decompose(gate):
    n = gate.shape[0]  # 量子门维度
    gate_0=gate   # 保存初始量子门的状态
    gate_vector=[]  # 分解得到的Givens矩阵按乘积顺序放在该数组里

    for i in range(n-1):
        for j in range(n-i-1):
            G=np.zeros((n,n),dtype=complex)
            for k in range(n):
                G[k][k]=1
            j_0 = n-j-1
            k_0=j_0-1
            i_0=i
            model=np.sqrt(np.abs(gate_0[j_0][i_0])**2+np.abs(gate_0[k_0][i_0])**2)
            if np.abs(gate_0[j_0][i_0])<=0.0001:
                gate_vector.insert(0,[G,[-1,-1]])
                continue
            G[k_0][k_0]=np.conj(gate_0[k_0][i_0]) / model
            G[k_0][j_0] = np.conj(gate_0[j_0][i_0]) / model
            G[j_0][k_0] = -gate_0[j_0][i_0] / model
            G[j_0][j_0] = gate_0[k_0][i_0] / model
            gate_0=G@gate_0
            if k_0>j_0:
                gate_vector.insert(0,[np.linalg.inv(G),[j_0,k_0]])
            else:
                gate_vector.insert(0, [np.linalg.inv(G), [k_0, j_0]])

    return [gate_vector,gate_0]


if __name__ == '__main__':
    [gate_vector_test,gate_test]=qrd_decompose(Test)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('off')
    tb=ax.table(cellText=gate_test.tolist(), loc='center')
    tb.auto_set_font_size(False)
    tb.set_fontsize(8)
    plt.show()
