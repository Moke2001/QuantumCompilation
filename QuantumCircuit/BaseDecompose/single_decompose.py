"""
函数：将一个单量子比特门完全分解
single_decompose(U:某个单量子门,num:量子门作用位置)  --->  result
result：量子门序列
"""
import numpy as np

from Tool.BaseGate import *
from QiskitInterface.operator import *


def single_decompose(U,num):

    ## 将量子门元素记录下来
    a = U[0][0];c = U[1][0]
    a1 = np.real(U[0][0]) ; a2 = np.imag(U[0][0])
    b1 = np.real(U[0][1]) ; b2 = np.imag(U[0][1])
    c1 = np.real(U[1][0]) ; c2 = np.imag(U[1][0])
    d1 = np.real(U[1][1]) ; d2 = np.imag(U[1][1])

    ## 如果第一个元素为0
    if a == 0:
        theta = np.pi

        ## c2=0的情况需要单独讨论
        if c2==0:
            if c1==1:
                wc=0
            elif c1==-1:
                wc=np.pi
        else:
            wc=np.arcsin(c2)

            ## b2=0的情况需要单独讨论
        if b2 == 0:
            if b1 == 1:
                wb = np.pi
            elif b1 == -1:
                wb = 0
        else:
            wb = np.arcsin(-b2)

        ## 计算结果
        delta = (wc+wb) / 2
        beta = 0
        alpha = wc-wb

    ## 如果第三个元素为0
    elif c == 0:
        theta = 0

        ## a2=0需要单独考虑
        if a2==0:
            if a1==1:
                wa=0
            elif a1==-1:
                wa=np.pi
        else:
            wa=np.arcsin(a2)

        ## d2=0需要单独考虑
        if d2==0:
            if d1==1:
                wd=0
            elif d1==-1:
                wd=np.pi
        else:
            wd=np.arcsin(d2)

        ## 计算结果
        delta = (wa+wd) / 2
        beta = 0
        alpha = wd-wa

    ## 正常情况
    else:
        theta = 2 * np.arctan(np.abs(a) / np.abs(c))

        ## a的分类讨论：
        if a2==0:
            if a1>0:
                wa=0
            if a1<0:
                wa=np.pi
        else:
            wa=np.arcsin(a2/np.cos(theta/2))

        ## c的分类讨论：
        if c2 == 0:
            if c1 > 0:
                wc = 0
            if c1 <0:
                wc = np.pi
        else:
            wc = np.arcsin(c2 / np.sin(theta / 2))

        ## d的分类讨论：
        if d2 == 0:
            if d1 >0:
                wd = 0
            if d1 <0:
                wd = np.pi
        else:
            wd = np.arcsin(d2 / np.cos(theta / 2))

        ## 计算结果
        alpha = wc-wa
        beta = wd-wc
        delta = (wd+wa)/2

    delta=delta-alpha/2-beta/2

    return [['RZ',[num,beta]],['RY',[num,theta]],['RZ',[num,alpha]],['I',[num,delta]]]  # 返回分解的结果


## 用于测试结果
if __name__ == '__main__':
    cache=H
    result_test = single_decompose(cache,0)  # 输出结果
    print(result_test)  # 打印结果
    output_operator(result_test,1)
    v=1+1