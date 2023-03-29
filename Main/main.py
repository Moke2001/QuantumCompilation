"""
主函数
"""
from Main.operator import output_operator
from QuantumCircuit.total_decompose import total_decompose
from Tool.BaseGate import Test


if __name__ == "__main__":
    gate_vector_test = total_decompose(Test)
    output_operator(gate_vector_test, 2)  # 输入为量子门的表示序列
