###-------------------- 字典函数 --------------------###
## 通过识别门的名字，执行相应的语句
from qiskit import QuantumCircuit


def dictionary(gate_name,vec,qc):
    try:
        if gate_name == 'H':  # Hadamard门
            num=vec[0]
            qc.h(num)
        elif gate_name == 'X':  # Pauli-X门
            num=vec[0]
            qc.x(num)
        elif gate_name == 'Y':  # Pauli-Y门
            num=vec[0]
            qc.y(num)
        elif gate_name == 'Z':  # Pauli-Z门
            num=vec[0]
            qc.z(num)
        elif gate_name == 'RX':  # RX旋转门
            num=vec[0]
            theta=vec[1]
            qc.rx(theta,num)
        elif gate_name == 'RY':  # RY旋转门
            num=vec[0]
            theta=vec[1]
            qc.ry(theta,num)
        elif gate_name == 'RZ':  # RZ旋转门
            num=vec[0]
            theta=vec[1]
            qc.rz(theta,num)
        elif gate_name == 'CZ':  # 受控Z旋转门
            control=vec[0]
            target=vec[1]
            qc.cz(control,target)
        elif gate_name == 'CX':  # 受控非门
            control=vec[0]
            target=vec[1]
            qc.cx(control,target)
        elif gate_name=='I':  # 全局相位门
            num=vec[0]
            theta=vec[1]
            qc.global_phase = theta  # 以弧度表示的旋转角度
        else:
            raise ValueError("输入的门不合法")  # 如果输入门不在集合中，则抛出异常信息
    except ValueError as e:
        print(e)  # 打印异常信息
