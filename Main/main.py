from qiskit import QuantumCircuit, Aer
from qiskit.quantum_info import Operator
import matplotlib.pyplot as plt
from Main.dictionary import dictionary
from QuantumCircuit.total_decompose import total_decompose
from Tool.BaseGate import Test


def main(gate_vector):
    ## 将门序列输入到量子线路中
    qc = QuantumCircuit(1, 1)  # 定义量子线路的量子比特与经典比特个数
    for i in range(len(gate_vector)):
        [gate_name, vec] = gate_vector[i]
        dictionary(gate_name,vec,qc)

    ## 将矩阵作为表格输出到图片中
    matrix = Operator(qc).data
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.axis('off')
    tb = ax.table(cellText=matrix, loc='center', cellLoc='center')
    tb.auto_set_font_size(False)
    tb.set_fontsize(8)
    plt.show()


if __name__ == "__main__":
    gate_vector_test=total_decompose(Test)
    main(gate_vector_test)  # 输入为量子门的表示序列
