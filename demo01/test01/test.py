import sys


def fibonacci(n):  # 生成器函数
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        print("-")
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(15)

while True:
    try:
        print(next(f), end=" ")

    except StopIteration:
        sys.exit()
