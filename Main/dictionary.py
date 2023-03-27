"""
函数：通过识别门的名字，执行相应的语句
"""


def dictionary(gate_name,vec,qc):

    try:

        ## Hadamard门
        if gate_name == 'H':
            num=vec[0]
            qc.h(num)

        ## Pauli-X门
        elif gate_name == 'X':
            num=vec[0]
            qc.x(num)

        # Pauli-Y门
        elif gate_name == 'Y':
            num=vec[0]
            qc.y(num)

        ## Pauli-Z门
        elif gate_name == 'Z':
            num=vec[0]
            qc.z(num)

        ## RX旋转门
        elif gate_name == 'RX':
            num=vec[0]
            theta=vec[1]
            qc.rx(theta,num)

        ## RY旋转门
        elif gate_name == 'RY':
            num=vec[0]
            theta=vec[1]
            qc.ry(theta,num)

        ## RZ旋转门
        elif gate_name == 'RZ':
            num=vec[0]
            theta=vec[1]
            qc.rz(theta,num)

        ## 受控Z旋转门
        elif gate_name == 'CZ':
            control=vec[0]
            target=vec[1]
            qc.cz(control,target)

        ## 受控非门
        elif gate_name == 'CX':
            control=vec[0]
            target=vec[1]
            qc.cx(control,target)

        ## 全局相位门
        elif gate_name=='I':
            theta=vec[1]
            qc.global_phase = theta  # 以弧度表示的旋转角度

        ## 如果输入门不在集合中，则抛出异常信息
        else:
            raise ValueError("输入的门不合法")

    ## 打印异常信息
    except ValueError as e:
        print(e)
