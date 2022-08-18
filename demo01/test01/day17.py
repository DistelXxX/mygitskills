"""
多态
    调用相同名称的方法，传入不同的参数对象，展现胡出不同的结果，这个叫做多态
    前提：首先要有继承关系,其次要有方法重写（多态的意义）
"""


class Father:
    def study(self):
        print("Father:Study!!!")


class Son(Father):
    def study(self):
        print('Son:Study!!!')


# if __name__ == "__main__":
#     def study(obj):
#         obj.study()
#
#
#     f = Father()
#     s = Son()
#
#     study(f)  # 调用父类的对象
#     study(s)  # 调用子类的对象

# if __name__ == "__main__":
#     def method(obj):
#         obj.study()
#
#
#     f = Father()
#     s = Son()
#
#     method(f)
#     method(s)

"""
重写：子类继承父类方法之后，父类不能满足子类需求，在子类当中重新定义与父类相同的名称的方法叫重写
重载：python没有重载，Java有重载——在同一个类中，定义同名的方法，参数的个数，顺序，类型不一致，这个叫做重载
"""


class Test:
    def method(self):
        print("method 1")

    def method(self, name):
        print("method %s" % name)

    def method(self, name, age):
        print("method %s %d" % (name, age))


if __name__ == "__main__":
    t = Test()
    t.method("lai", 12)  # 只有method(self)一个函数，没有重载
