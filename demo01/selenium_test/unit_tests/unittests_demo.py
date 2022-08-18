# coding=utf-8
import unittest

first = 20


class TestStorm(unittest.TestCase):
    a = 4

    def setUp(self):  # 在每个测试用例执行前执行一次
        print('setUp')

    @unittest.skip(a > 3, 'info')
    # @unittest.skipUnless(a==5,'info')
    def test_age(self):  # 方法名使用小写字母，且以test开头
        second = first + 5  # 用例操作
        self.assertEqual(second, 25)  # 操作结果断言

    @unittest.skip('skip info')
    def test_name(self):
        print('laiyongjun')

    def tearDown(self):  # 在每个测试用例后执行一次
        print('tearDown')


# if __name__ == '__main__':
#     unittest.main()

# if __name__ == '__main__':
#     testcase = unittest.TestLoader().loadTestsFromTestCase(TestStorm)
#     suite = unittest.TestSuite([testcase])
#     unittest.TextTestRunner.run(suite)

# if __name__ == "__main__":
#     suite = unittest.TestSuite()
#     suite.addTest(TestStorm.TestFirst('test_age'))
#     suite.addTest(TestStorm.TestSecond('test_name'))
#     unittest.TextTestRunner().run(suite)

# 其实测试用例执行的顺序依照的是方法和函数名的ASCII值排序。

if __name__ == '__main__':
    testSuite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(testSuite)




