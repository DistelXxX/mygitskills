# coding=gbk
# �������ݿ�

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
        #         sql =sql+ '(' + str(i) + ',"�������");'
        #         #(id,"classname")
        #     elif i==5:
        #         a= 1/0
        #         sql += '(' + str(i) + ',"�������"),'
        # print(sql)
        # print(type(sql))

        sql = 'select *from qq_email where username = %s'

        try:
            # ִ��SQL���
            t = cursor.execute(sql, username)
            # �ύ������commit()����ʹ���ݿ�����Ӧ�ĸ��ģ������ò������ģ���Ҳ���ᱨ��
            # mydb.commit()
            results = cursor.fetchall()
            print('�ɹ�')
            # print(results)
            list01 = []
            for i in results:
                for j in i:
                    list01.append(j)
            # print(list01)
            return list01
        except:
            # ��������ʱ�ع�
            # mydb.rollback()
            print('ʧ��')
        # �ر��α꣨��ִ��Ҳ���ԣ�
        cursor.close()

        # �ر����ݿ����ӣ���ִ��Ҳ���ԣ�
        mydb.close()


if __name__ == '__main__':
    a = UandP()
    b = a.getUsernameAndPassword('15970926681')
    # print(b)
