# coding=utf-8

import pytest

# class TestWangyi():

def setup_module():
    print('setup_module')

def teardown_module():
    print('teardown_module')

# def setup():
def setup_function():
    print('setup_fuction')

# def teardown():
def teardown_function():
    print('teardown_fuction')

def test_a():
    print("aaaaa")
    assert "a" == "a"

def test_b():
    print("bbbbb")
    assert "b" == "b"


if __name__ == '__main__':
    # pytest.main(['-s','test_demo01.py'])

    # 对于Pytest框架代码，你可以不把测试用例放置到class中，而是直接定义函数。
    pytest.main(['-s'])