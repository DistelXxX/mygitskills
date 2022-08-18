# coding=utf-8
# 使用range（）批量插入数据方法二：
import pymysql
import random
class DatabaseAccess():
	#初始化属性
    def __init__(self):
        self.__db_host = "localhost"
        self.__db_port = 3306
        self.__db_user = "root"
        self.__db_password = "123456"
        self.__db_database = "testdb"
	#链接数据库
    def isConnectionOpen(self):
        self.__db = pymysql.connect(
            host=self.__db_host,
            port=self.__db_port,
            user=self.__db_user,
            password=self.__db_password,
            database=self.__db_database,
            charset='utf8'
        )
	#插入数据
    def linesinsert(self,age,name):
        try:
            #连接数据库
            self.isConnectionOpen()
            # 创建游标
            global cursor
            cursor = self.__db.cursor()
            # sql命令
            sql = "insert into classes(cid,classname) value(%s,%s)"
            # 执行sql命令
            cursor.execute(sql, (age, name))
        except Exception as e:
            print(e)
        finally:
            # 关闭游标
            cursor.close()
            # 提交
            self.__db.commit()
            # 关闭数据库连接
            self.__db.close()
	#数据生成，姓名，年龄，并调用数据插入方法
    def data_update(self):
        ret1 = random.choice(['张','刘','王'])
        ret2 = random.choice(['中','红','海'])
        name = ret1 + ret2
        age = random.randint(10, 20)
        self.linesinsert(age, name)

if __name__ == "__main__":
	#创建实例化对象
    db=DatabaseAccess()
    #循环10次，插入10条数据
    for record in range(1,11):
    	#调用方法
        db.data_update()


#直接插入数据
#连接数据库
db=pymysql.connect(host='localhost',user='root',password='root',database='test')

#使用cursor()方法获取操作游标
cursor=db.cursor()


