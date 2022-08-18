# coding=gbk
# 连接数据库

import pymysql
import random


class UandP:
    def getUsernameAndPassword(self, username):
        mydb = pymysql.connect(host='localhost',
                               user='root',
                               port=3306,
                               passwd='123456',
                               database='test')

        cursor = mydb.cursor()

        # sql = 'insert into classes(cid,classname) values'
        #
        # for i in range(10):
        #     if i == 9:
        #         sql =sql+ '(' + str(i) + ',"软件测试");'
        #         #(id,"classname")
        #     elif i==5:
        #         a= 1/0
        #         sql += '(' + str(i) + ',"软件测试"),'
        # print(sql)
        # print(type(sql))

        sql = 'select *from qq_email where username = %s'

        try:
            # 执行SQL语句
            t = cursor.execute(sql, username)
            # 提交（调用commit()方法使数据库做相应的更改；不调用不做更改，但也不会报错）
            # mydb.commit()
            results = cursor.fetchall()
            print('成功')
            # print(results)
            list01 = []
            for i in results:
                for j in i:
                    list01.append(j)
            # print(list01)
            return list01
        except:
            # 发生错误时回滚
            # mydb.rollback()
            print('失败')
        # 关闭游标（不执行也可以）
        cursor.close()

        # 关闭数据库连接（不执行也可以）
        mydb.close()


if __name__ == '__main__':
    a = UandP()
    b = a.getUsernameAndPassword('15970926681')
    # print(b)
