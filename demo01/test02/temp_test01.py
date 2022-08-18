# # coding=utf-8
# from collections import Counter
# a = 'abbccd'
# # 首先统计字符的出现的次数
# a= Counter(a)
# print(a)
# # 转化成字典格式
# dict = dict(a)
# # 取出最小的values值
# min_key = min(dict.values())
# #print(min_key)
# # 遍历key值
# for i in dict.keys():
#     # 查看对应的值是否==最小的值 ，等于则取出值出来
#     if dict[i] == min_key:
#         print(i)
from test02.temp_test02 import A


class B(A):
    # def __init__(self):
    #     self.n = 3

    def sum(self, m):
        m=super().sum(m)
        print(self.__n)
        return self.__n + m


if __name__ == "__main__":
    b = B()
    print(b.sum(3))
