"""
类：二进制类
class Binary{
n：二进制串长度
vec：二进制串表示
value：二进制串对于十进制数值
}
"""


class Binary:

    ### 构造函数 ###
    def __init__(self, argument, n):
        if isinstance(argument, list):
            self.n = len(argument)  # 二进制串的长度
            self.vec = argument  # 二进制串的表示
            moment = 0
            for i in range(self.n):
                moment = moment + (2 ** i) * argument[self.n - i - 1]
            self.value = moment  # 二进制串对应的十进制数
        elif isinstance(argument, int):
            binary_str = bin(argument)[2:]  # 将十进制数转换为二进制字符串，去掉前缀"0b"
            bin_array = [int(x) for x in binary_str]  # 将二进制字符串转换为01数组
            self.vec = bin_array  # 二进制串的表示
            self.n = len(self.vec)  # 二进制串的长度
            self.value = argument  # 二进制串对应的十进制数

        ## 如果位数不够，在前面补齐零
        if n > self.n:
            self.vec = ([0] * (n - self.n)) + self.vec
            self.n = n

    ## 重载加法运算符
    def __add__(self, x):
        a = self.value  # 记录被加数的十进制数
        b = x.value  # 记录加数的十进制数
        return Binary(a + b, 0)  # 返回二进制对象

    ## 重载减法运算符
    def __sub__(self, x):
        a = self.value  # 记录被减数的十进制数
        b = x.value  # 记录减数的十进制数
        return Binary(a - b, self.n)  # 返回二进制对象

    ## 重载输出运算符
    def __str__(self):
        print("二进制表示为：" + str(self.vec))
        print("十进制表示为：" + str(self.value))
        return "Over"

    ## 重载复制运算符
    def copy(self):
        return Binary(self.vec.copy(), self.n)

    ## 改变某一位上的数
    def change(self, n):
        if self.vec[n] == 1:
            self.vec[n] = 0  # 改变二进制数组中下标为n的数
        else:
            self.vec[n] = 1  # 改变二进制数组中下标为n的数

    ## 输出某一位上的数
    def output(self, n):
        return self.vec[n]  # 返回二进制数组中下标为n的数


if __name__ == "__main__":
    x = Binary([0, 1, 0, 1], 5)
    print(x)
