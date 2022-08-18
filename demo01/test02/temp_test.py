# name = 'laiyongjun'
#
# name = list(name)
# print(name)
# name = name[-1::-1]
# print(name)
#
#
# for i in range(1,99):
#     print(i)


# tuple01 = (1,2,3)
# print(type(tuple01))
# print(tuple01)
#
# set01 = {"qwe","qwe","rty"}
# # print(set01)
# #
# list01 = ["qwe","qwe","rty"]
# # list01 = set(list01)
# # print(list01)
#
# list01[0] = "wer"
# print(list01)

# dict01 = {"qwe":123}
#
# print(dict01["qwe"])
#
# name = 'lyj'
# new_name = name.center(20,'*')
# print(new_name)


list01 = (1,2,3,4,5)
# dict01 = dict()
#
# for i in list01:
#     dict01[list01.index(i)]=i
# print(dict01)

dict01 = dict(zip(range(0,len(list01)),list01))
print(dict01)


s = "QWERTYUIO"

dict02 = dict(s)
print(dict02)








