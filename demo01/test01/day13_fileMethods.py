#coding=utf-8
#定义成读写方法
def write_txt(file_name,content):
    with open(file_name,'a') as f:
        f.write(content)

def read_txt(file_name):
    with open(file_name,'r')as f:
        result = f.read().splitlines()
        return result

if __name__ == '__main__':
    write_txt('1.txt',"\nqwertyuiop\n")
    result  = read_txt('1.txt')
    print(result)