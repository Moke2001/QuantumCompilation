"""
主函数
"""

from QuantumCircuit.total_decompose import *
from Tool.BaseGate import *


if __name__ == "__main__":
    gate_vector_test = total_decompose(Test)
    matrix_show(Test)
    output_operator(gate_vector_test, 2)  # 输入为量子门的表示序列
    x=1
