#coding=utf-8
#csv写成读写的方法
import csv

def write_csv(file_name,content):
    with open(file_name,'a',newline='') as file1:
        obj = csv.writer(file1)
        obj.writerow(content)


def read_csv(file_name):
    result = []
    with open(file_name,'r',newline='') as file2:
        obj = csv.reader(file2)
        for i in obj:
            result.append(i)
    return result


if __name__ == '__main__':
    # write_csv('study1.csv',['5','赖永军','22'])

    result = read_csv('study1.csv')
    print(result)
    print(type(result))
    print(result[1][1])