#coding=utf-8
"""
继承
    至少基于两个类之间才有继承
"""
class Father:
    name1 = "老张"
    def eat(self):
        print("father,eat!!!")

class Son(Father):#继承，子类（派生类），支持多继承，调用规则，从左到右，从深度到广度
    name = "小张"
    def eat1(self):
        print("Son,eat!!!")

if __name__=="__main__":
    # a = Son()
    # print(a.name)
    # a.eat1()

    # b = Father()
    # print(b.name)
    # b.eat()

    #继承
    c = Son()
    print(c.name)
    print(c.name1)
    c.eat()

#定义类方式
#父类要定义在子类的前面
#父类和子类的方法名相同，则子类对父类的方法进行了重写

#调用父类的方法：super().method()
#self.method()不推荐，子类中重写了父类的方法就不会调用父类的方法




