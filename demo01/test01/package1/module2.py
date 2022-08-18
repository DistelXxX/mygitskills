class Test01:
    def method3(self):
        print('method3')

    def method4(self):
        print('method4')

class Test02:
    def method5(self):
        print('method5')

    def method6(self):
        print('method6')


if __name__ == '__main__':
    t1 = Test01()
    t1.method3()
    t1.method4()

    t2 = Test02()
    t2.method5()
    t2.method6()