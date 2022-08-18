# coding=utf-8
import pytest


class Test_test02():
    def setup_class(self):
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')

    # def setup_method(self):
    def setup(self):
        print('setup_method')
    # def teardown(self):
    def teardown_method(self):
        print('teardown_method')

    def test_a(self):
        print("aaaaa")
        assert "a" == "a"  # '.'代表断言成功

    def test_b(self):
        print("bbbbb")
        assert "b" == "b"

if __name__ == '__main__':
    pytest.main(['-s','test_demo02.py'])
    # pytest.main(['-s'])
    # 使用pytest.main(["-s"])执行当前文件所在目录下所有符合条件的测试用例