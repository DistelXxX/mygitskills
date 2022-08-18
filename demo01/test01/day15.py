#coding=utf-8
"""
面向对象
类
对象
属性
方法
"""

# #定义一个类
# class Person:
#     name = 'zhangsan'
#     __age = 18#“__”双下划线表示私有化,只能该类自己调用，外部类不能调用
#
#     def study(self):
#         print('study')
#         print(self.name)
#         print(self.__age)
#     def __sleep(self):
#         print('sleep')
#
#
# if __name__ == "__main__":
#     p = Person()#实例化Person类得到一个对象
#     print(p.name)#调用累的属性
#     # print(p.age)
#     p.study()#调用类的方法


"""
构造方法和析构方法
"""
class Person:
    def __init__(self):#构造方法：在类实例化的时候最先执行，通常用来初始化一些对象
        # print("我是构造方法")
        self.name = 'zhangsan'
        self.age = 18#属性定义在方法中需要加self，如果定义在类中方法的外面，不需要加self
    def study(self):
        print('study')
    def sleep(self):
        print('sleep')

    def __del__(self):#析构方法，在类的实例化的时候，通常最后执行，用来回收对象，释放资源
        # print("我是析构方法")
        del self.name
        del self.age#删除对象属性，释放资源

if __name__ == '__main__':
    # p = Person()#实例化会自动执行构造方法和析构方法
    # p.study()
    # p.sleep()

    Person().study()
    Person().sleep()






