###-------------------- 字典函数 --------------------###
## 通过识别门的名字，执行相应的语句


def dictionary(gate_name):
    try:
        if gate_name == 'H':  # Hadamard门
            s_1="num=vec[0]"
            s_2="qc.h(num)"
            s_3 = "pass"
        elif gate_name == 'X':  # Pauli-X门
            s_1 = "num=vec[0]"
            s_2 = "qc.x(num)"
            s_3 = "pass"
        elif gate_name == 'Y':  # Pauli-Y门
            s_1 = "num=vec[0]"
            s_2 = "qc.y(num)"
            s_3 = "pass"
        elif gate_name == 'Z':  # Pauli-Z门
            s_1 = "num=vec[0]"
            s_2 = "qc.z(num)"
            s_3 = "pass"
        elif gate_name == 'RX':  # RX旋转门
            s_1 = "num=vec[0]"
            s_2 = "theta=vec[1]"
            s_3 = "qc.rx(theta,num)"
        elif gate_name == 'RY':  # RY旋转门
            s_1 = "num=vec[0]"
            s_2 = "theta=vec[1]"
            s_3 = "qc.ry(theta,num)"
        elif gate_name == 'RZ':  # RZ旋转门
            s_1 = "num=vec[0]"
            s_2 = "theta=vec[1]"
            s_3 = "qc.rz(theta,num)"
        elif gate_name == 'CZ':  # 受控Z旋转门
            s_1 = "control=vec[0]"
            s_2 = "target=vec[1]"
            s_3 = "qc.cz(control,target)"
        elif gate_name == 'CX':  # 受控非门
            s_1 = "control=vec[0]"
            s_2 = "target=vec[1]"
            s_3 = "qc.cx(control,target)"
        elif gate_name=='I':  # 全局相位门
            s_1="qc.globalphase(theta)"
            s_2="pass"
            s_3="pass"
        else:
            raise ValueError("输入的门不合法")  # 如果输入门不在集合中，则抛出异常信息
        return [s_1, s_2, s_3]
    except ValueError as e:
        print(e)  # 打印异常信息
