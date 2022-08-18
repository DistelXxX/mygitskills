# import sys
# for i in sys.argv:
#     print(i)

# def print_func(par):
#     print("hello:%s"%par)
#     return
#
# def area(width,height):
#     """
#     :param width:
#     :param height:
#     :return:
#     """
#     return width*height
#
# w = 4
# h = 5
# print(area(4,5))
# print_func("lailai")

# if __name__ == '__main__':
#     print_func("lailai")

######################不定长参数########################
def add(*number):
    total = 0
    for i in number:
        # print(i)
        total = total + i

    return total


if __name__ == '__main__':
    # add(1, 2, 3)
    print(add(1,2,3))