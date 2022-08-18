# coding=utf-8
'''
class Animal:
    def __init__(self):
        self.__name = 'Tom'  # 私有属性
        self.age = 3  # 普通属性

    def __get_name(self):  ##私有方法
        print("名字是{0}".format(self.__name))

    def get_age(self):  # 普通方法,可以调用私有属性和方法
        print("{0} 的年龄是{1}岁".format(self.__name, self.age))


cat = Animal()
cat.get_age()  # 调用get_age()
cat._Animal__get_name()
'''


# 外界无法访问私有方法，但可以在类内部方法私有方法。

class A():
    def __init__(self):
        self.__n = 2

    def sum(self, m):
        print(m)

        return self.__n+m


class B(A):
    # def __init__(self):
    #     self.n = 3

    def sum(self, m):
        m=super().sum(m)
        print(self.n)
        return self.n + m


if __name__ == "__main__":
    b = B()
    print(b.sum(3))
