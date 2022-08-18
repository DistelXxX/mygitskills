"""
异常捕获

    错误：语法错误
    异常：指的是程序运行时除语法错误外的错误
        除数为零异常
        类型异常
        命名异常
        ...
"""
import sys

# 异常捕获
try:
    print('123456')
    # print(1 / 0)
    # print(1+'a')
    print('789-')

# except ZeroDivisionError as e:  # 捕获除数为零异常
#     print(e)
#
# except NameError as e:
#     print(e)

# except (ZeroDivisionError, NameError) as e:  # 同时捕获多个异常
#     print(e)

# except:
#     print(sys.exc_info())  # 捕获所有已知和未知的异常，不推荐，因为这种捕获方式可能会隐藏更深层次的问题

except Exception as e:
    print(e)
    # pass  # 不打印异常
    # 这里通常会写一个写好的截图或写日志的方法（自动化脚本阶段）
else:
    print('else')  # 没有异常才会执行
finally:
    print('finally')  # 有没有异常都会执行

print("789-")


#使用了自定义异常
for i in range(1,11):
    if i == 5:
        try:
            raise TypeError('自定义异常')
        except Exception as e:
            print(e)

    else:
        print(i)


for i in range(1,11):
    if i == 5:
        # continue  # 结束本轮循环，进行下一循环
        # pass  # 空语句
        break  #结束循环
    else:
        print(i)

    print('11111111111')
