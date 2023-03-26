###-------------------- 将一个Toffoli门分解 --------------------###
## 将一个Toffoli门完全分解
from cu_decompose import *


def toffoli_decompose(c_1,c_2,target):
    V=np.array([[1,1j],[1j,1]])/(1+1j)
    result = cu_decompose([[c_2,target],V]) + [['CX',[c_1,target]]] + cu_decompose([[c_2,target],V.conj().T]) +[['CX',[c_1,target]]]
    return result


if __name__=="__main__":
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    concatenated_list = list1 + list2
    print(concatenated_list)
