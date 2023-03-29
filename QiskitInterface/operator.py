"""
函数：输入量子门序列，返回作用的矩阵
output_operator(gate_vector:矩阵序列,n:量子比特的个数)  --->  plt.show()
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
import matplotlib.pyplot as plt
from QiskitInterface.dictionary import dictionary
from QiskitInterface.matrix_show import matrix_show


def output_operator(gate_vector,n):

    qc = QuantumCircuit(n,n)  # 定义量子线路的量子比特与经典比特个数

    ## 解码门序列矩阵
    for i in range(len(gate_vector)):
        [gate_name, vec] = gate_vector[i]  # 输出门序列元
        dictionary(gate_name,vec,qc)  # 调用字典函数解码门序列元

    ## 将矩阵作为表格输出到图片中
    matrix = Operator(qc).data
    matrix_show(matrix)



## 用于测试结果
if __name__ == "__main__":
    pass
