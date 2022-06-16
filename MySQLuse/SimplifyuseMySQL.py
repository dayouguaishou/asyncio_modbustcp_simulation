#coding: utf-8
'''
20200318 for Python3 by Wei.Wei
#cnf.ini
[db]
db_host = 192.168.137.137
db_port = 3306
db_user = root
db_pass = root@123
db_name = test

函数名称：cnfdb(filename = "cnf.ini")
说明：从filename文件中获取mysql连接参数
返回：dictionary（字典）-cnfg_dict{}

函数名称：select_MYSQL(SQL,filename = "cnf.ini"):
说明：指定配置文件（filename）查询数据库
返回：数据集（元组）-datas() 或输出错误信息

函数名称：select_datas_column(datas,num = 0)
说明：查询数据集某一列（num）num>=0
返回：数据列（list）-list[]

函数名称：execute_to_mysql(SQL,filename = "cnf.ini"):
说明：指定配置文件（filename）执行SQL语句
返回：无 或输出错误信息
'''

#import MySQLdb as mdb
import pymysql
#import ConfigParser
#from configparser import ConfigParser
import configparser
import sys,os

def cnfdb(filename = "cnf.ini"):
    cf = configparser.ConfigParser()
    cf.read(os.path.dirname(os.path.abspath(__file__))+'/'+filename)
    cnfg = []
    cnfname = ["db_host","db_user","db_pass","db_name","db_port"]
    for keys in cnfname:
        cnfg.append(cf.get("db", keys))
    cnfg_dict = dict(zip(cnfname, cnfg))
    return cnfg_dict

def select_MYSQL(SQL,filename = "cnf.ini"):
    conf = cnfdb(filename)
    try:
        conn = pymysql.Connect(host=conf["db_host"] , port = int(conf["db_port"]) , user=conf["db_user"], passwd=conf["db_pass"], db=conf["db_name"], charset='utf8')
        cursor = conn.cursor()
        cursor.execute(SQL)
        nums = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
    except IOError as e:
        print ("Error (0) %d: %s" % (e.args[0], e.args[1]))
        sys.exit(0)
    return nums

def select_datas_column(datas,num = 0):
    list = []
    for i in range(len(datas)):
         list.append(datas[i][num])
    return list


def execute_to_mysql(SQLS,filename = "cnf.ini"):
    conf = cnfdb(filename)
    try:
        conn = pymysql.Connect(host=conf["db_host"] , port = int(conf["db_port"]) , user=conf["db_user"], passwd=conf["db_pass"], db=conf["db_name"], charset='utf8')
        cursor = conn.cursor()
        cursor.execute(SQLS)
        conn.commit()
        cursor.close()
        conn.close()
    except pymysql.Error as e:
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)



if __name__ == '__main__':
    print(cnfdb())
    print(select_MYSQL("SELECT * FROM dailiip"))
