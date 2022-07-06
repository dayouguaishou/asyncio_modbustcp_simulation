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

函数名称：getConfig(filename = "cnf.ini", section="db")
说明：从filename文件中获取mysql连接参数
filename：该参数可以是配置文件的路径
section：该参数是配置文件下的项目名称
返回：dictionary（字典）-cnfg_dict{}

函数名称：select_MYSQL(SQL,filename = "cnf.ini", section="db"):
说明：指定配置文件（filename）查询数据库
filename：该参数可以是配置文件的路径
section：该参数是配置文件下的项目名称
返回：数据集（元组）-datas() 或输出错误信息

函数名称：select_datas_column(datas,num = 0)
说明：查询数据集某一列（num）num>=0
返回：数据列（list）-list[]

函数名称：execute_to_mysql(SQL,filename = "cnf.ini", section="db"):
说明：指定配置文件（filename）执行SQL语句
filename：该参数可以是配置文件的路径
section：该参数是配置文件下的项目名称
返回：无 或输出错误信息
'''

#import MySQLdb as mdb
import pymysql
#import ConfigParser
#from configparser import ConfigParser
import configparser
import sys,os

def getConfig(filename = "cnf.ini", section="db"):
    """
    :param filename 文件名称
    :param section: 服务
    :return:返回配置信息(config_dic)
    """
    if "/" in filename or "\\" in filename:
        proDir = filename
    else:
        proDir = os.path.split(os.path.realpath(__file__))[0]
    configPath = os.path.join(proDir, filename)
    conf = configparser.ConfigParser()
    conf.read(configPath)
    config = conf.items(section)
    config_dic = {}
    for tups in config:
        config_dic.update({tups[0]:tups[1]})
    return config_dic

def select_MYSQL(SQL,filename = "cnf.ini",section="db"):
    conf = getConfig(filename,section)
    try:
        conn = pymysql.Connect(host=conf["db_host"] , port = int(conf["db_port"]) , user=conf["db_user"], passwd=conf["db_pass"], db=conf["db_name"], charset='utf8')
        cursor = conn.cursor()
        cursor.execute(SQL)
        nums = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
    except IOError as e:
        print ("Error (select_MYSQL) %d: %s" % (e.args[0], e.args[1]))
        sys.exit(0)
    return nums

def select_datas_column(datas,num = 0):
    list = []
    for i in range(len(datas)):
         list.append(datas[i][num])
    return list


def execute_to_mysql(SQLS,filename = "cnf.ini",section="db"):
    conf = getConfig(filename,section)
    try:
        conn = pymysql.Connect(host=conf["db_host"] , port = int(conf["db_port"]) , user=conf["db_user"], passwd=conf["db_pass"], db=conf["db_name"], charset='utf8')
        cursor = conn.cursor()
        cursor.execute(SQLS)
        conn.commit()
        cursor.close()
        conn.close()
    except pymysql.Error as e:
        print ("Error (execute_to_mysql)%d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

def execute_SQLlist_to_mysql(SQLlist=[],filename = "cnf.ini",section="db"):
    conf = getConfig(filename,section)
    try:
        conn = pymysql.Connect(host=conf["db_host"] , port = int(conf["db_port"]) , user=conf["db_user"], passwd=conf["db_pass"], db=conf["db_name"], charset='utf8')
        cursor = conn.cursor()
        for SQLS in SQLlist:
            cursor.execute(SQLS)
        conn.commit()
        cursor.close()
        conn.close()
    except pymysql.Error as e:
        print ("Error (execute_SQLlist_to_mysql)%d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)


if __name__ == '__main__':
    print(getConfig(section="db2"))
    execute_SQLlist_to_mysql(section="db2",SQLlist=[
        "UPDATE thtf_table_ai SET  ZHI='100.55' WHERE MING_CHENG='1'",
        "UPDATE thtf_table_ai SET  ZHI='101.55' WHERE MING_CHENG='2'",
        "UPDATE thtf_table_ai SET  ZHI='99.55' WHERE MING_CHENG='3'",
    ])
    print(select_MYSQL("SELECT * FROM thtf_table_ai LIMIT 3", section="db2"))
