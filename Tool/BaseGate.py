"""
库：常用的量子门的矩阵形式
"""

from Tool.dimension_change import *
import numpy as np


## Pauli-X门
def X_n(num,location):
    X_0 = np.array([[0., 1.], [1., 0.]])
    return dimension_change(X_0,  num, [location])


## Pauli-Y门
def Y_n(num, location):
    Y_0 = np.array([[0., -1.j], [1.j, 0.]])
    return dimension_change(Y_0,  num, [location])


### Pauli-Z门
def Z_n(num, location):
    Z_0 = np.array([[1., 0.], [0., -1.]])  # Pauli-Z门
    return dimension_change(Z_0, num, [location])


## Hadamard门
def H_n(num, location):
    H_0 = np.array([[1., 1.], [1., -1.]]) * (1. / np.sqrt(2.))  # Hadamard门
    return dimension_change(H_0, num, [location])


## 相位门
def S_n(num, location):
    S_0 = np.array([[1., 0.], [0, 1.j]])
    return dimension_change(S_0, num, [location])


## T门
def T_n(num, location):
    T_0 = np.array([[1., 0.], [0., np.exp(1.j * np.pi / 4.)]])  # T门
    return dimension_change(T_0, num, [location])


## RX门
def RX_n(theta,num,location):
    RX_0=np.array([[np.cos(theta / 2), -1j * np.sin(theta / 2)], [-1j * np.sin(theta / 2), np.cos(theta / 2)]])
    return dimension_change(RX_0, num, [location])


## RY门
def RY_n(theta,num,location):
    RY_0=np.array([[np.cos(theta / 2), -np.sin(theta / 2)], [np.sin(theta / 2), np.cos(theta / 2)]])
    return dimension_change(RY_0, num, [location])


## RZ门
def RZ_n(theta,num,location):
    RZ_0=np.array([[np.exp(-1j * theta / 2), 0], [0, np.exp(1j * theta / 2)]])
    return dimension_change(RZ_0, num, [location])


## 受控非门
def CNOT_n(num,location_c,location_not):
    CNOT_0=np.array([
        [1., 0., 0., 0.],
        [0., 1., 0., 0.],
        [0., 0., 0., 1.],
        [0., 0., 1., 0.]
    ])
    CNOT_1=np.array([
        [1., 0., 0., 0.],
        [0., 0., 0., 1.],
        [0., 0., 1., 0.],
        [0., 1., 0., 0.]
    ])
    try:
        if location_c<location_not:
            return dimension_change(CNOT_0, num, [location_c,location_not])
        elif location_c>location_not:
            return dimension_change(CNOT_1, num, [location_c,location_not])
        else:
            raise ValueError("输入的参数有误")  # 如果输入参数有误，则抛出异常信息
    except ValueError as e:
        print(e)  # 打印异常信息


## 受控Z门
def CZ_n(num, control, operator):
    CZ_0 = np.array([
        [1., 0., 0., 0.],
        [0., 1., 0., 0.],
        [0., 0., 1., 0.],
        [0., 0., 0., -1.]
    ])
    CZ_1=np.array([
        [1., 0., 0., 0.],
        [0., 1., 0., 0.],
        [0., 0., 1., 0.],
        [0., 0., 0., -1.]
    ])
    try:
        if control<operator:
            return dimension_change(CZ_0, num, [control, operator])
        elif control>operator:
            return dimension_change(CZ_1, num, [control, operator])
        else:
            raise ValueError("输入的参数有误")  # 如果输入参数有误，则抛出异常信息
    except ValueError as e:
        print(e)  # 打印异常信息


## 交换门
def SWAP_n(num,location_1,location_2):
    SWAP_0= np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ])
    return dimension_change(SWAP_0, num, [location_1,location_2])


## Toffoli门
def TO_n(num,location_c_1,location_c_2,location_g):
    TO_0= np.array([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0]
    ])
    TO_1 = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0]
    ])
    TO_2 = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0]
    ])
    try:
        if location_g>location_c_1 and location_g>location_c_2:
            return dimension_change(TO_0, num, [location_c_1, location_c_2,location_g])
        elif location_c_1 < location_g < location_c_2:
            return dimension_change(TO_1, num, [location_c_1, location_g, location_c_2])
        elif location_c_2 < location_g < location_c_1:
            return dimension_change(TO_1, num, [location_c_2, location_g, location_c_1])
        elif location_g < location_c_2 and location_g < location_c_1:
            return dimension_change(TO_2, num, [location_c_2, location_g, location_c_1])
        else:
            raise ValueError("输入的参数有误")  # 如果输入参数有误，则抛出异常信息
    except ValueError as e:
        print(e)  # 打印异常信息


### -----------------------下面的都是简单门-------------------------- ###


## Pauli-X门
X = np.array([[0., 1.], [1., 0.]])


## Pauli-Y门
Y = np.array([[0., -1.j], [1.j, 0.]])


## Pauli-Z门
Z = np.array([[1., 0.], [0., -1.]])


## Hadamard门
H = np.array([[1., 1.], [1., -1.]]) * (1. / np.sqrt(2.))


## 相位门
S = np.array([[1., 0.], [0, 1.j]])


## T门(一般形式)
T = np.array([[1., 0.],
              [0., np.exp(1.j * np.pi / 4.)]])


## RX门
def RX(theta):
    return np.array([[np.cos(theta / 2), -1j * np.sin(theta / 2)],
                     [-1j * np.sin(theta / 2), np.cos(theta / 2)]])


## RY门
def RY(theta):
    return np.array([[np.cos(theta / 2), -np.sin(theta / 2)],
                     [np.sin(theta / 2), np.cos(theta / 2)]])


## RZ门
def RZ(theta):
    return np.array([[np.exp(-1j * theta / 2), 0],
                     [0, np.exp(1j * theta / 2)]])


## CNOT门
CNOT=np.array([
    [1., 0., 0., 0.],
    [0., 1., 0., 0.],
    [0., 0., 0., 1.],
    [0., 0., 1., 0.]
    ])

## 受控Z门
CZ = np.array([
    [1., 0., 0., 0.],
    [0., 1., 0., 0.],
    [0., 0., 1., 0.],
    [0., 0., 0., -1.]
])

## 交换门
SWAP = np.array([
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1]
])


## Toffoli门
TO = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
])


## 两比特测试门
Test=np.array([
    [1/np.sqrt(2),       0,          1/np.sqrt(2),               0],
    [       0,                1,                0,                        0],
    [-1/np.sqrt(2),      0,        1/np.sqrt(2),                0],
    [       0,                0,               0,                         1],
])


## Givens测试门
givens_test=np.array([
    [1/np.sqrt(2),       0,                  0,       1/np.sqrt(2)],
    [       0,                1,                0,                        0],
    [       0,                0,                1,                        0],
    [-1/np.sqrt(2),      0,               0,                   1j/np.sqrt(2)],
])