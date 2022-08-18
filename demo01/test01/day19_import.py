# coding=utf-8
"""
导包，调用其他包的模块
"""
# import test01.package1.module1 as m1
# if __name__ == "__main__":
#     # test01.package1.module1.method1()  #  No module named 'test01.package1'; 'test01' is not a package
#     m1.method1()
#     m1.method2()

# from test01.package1.module1 import method1
# from test01.package1.module1 import method2
# from test01.package1.module1 import *
# if __name__ == "__main__":
#     method1()
#     method2()

# from test01.package1.module2 import Test01
# from test01.package1.module2 import Test02
# from test01.package1.module2 import Test01,Test02
# if __name__ == "__main__":
#     t1 = Test01()
#     t1.method3()
#     t1.method4()
#
#     t2 = Test02()
#     t2.method5()
#     t2.method6()

import csv


class Test:
    def read_csv(self, file_name):
        result = []
        with open(file_name, 'r') as f:
            obj = csv.reader(f)
            for i in obj:
                result.append(i)
        return result


if __name__ == "__main__":
    result = Test().read_csv('./data/study1.csv')
    print(result)
    print(type(result))
