基于Python3的对MySQL的简易查询模块
==================================================  
20200318 for Python3 by Wei.Wei

1.导入pymysql、configparser库  
1.1 Linux  
```
sudo pip3 install pymysql
```  
```
sudo pip3 install configparser
```   
1.2 Windows  
```
pip3 install pymysql
```  
```
pip3 install configparser
```   

2.cnf.ini 文件内容  
[db]  
db_host = 192.168.137.137  
db_port = 3306  
db_user = root  
db_pass = root@123  
db_name = test  

3.函数说明  

3.1 cnfdb(filename = "cnf.ini")  
----
说明：从filename文件中获取mysql连接参数  
返回：dictionary（字典）-cnfg_dict{}  

3.2 select_MYSQL(SQL)  
----
说明：查询数据库  
返回：数据集（元组）-datas() 或输出错误信息  

3.3 select_datas_column(datas,num = 0)  
----
说明：查询数据集某一列（num）num>=0  
返回：数据列（list）-list[]  

3.3 execute_to_mysql(SQLS)  
----
说明：执行SQL语句  
返回：无 或输出错误信息  

4.调用示例
```Python
import SimplifyuseMySQL

#查询
datas = SimplifyuseMySQL.select_MYSQL(SQL = "SELECT * FROM hour1 ")
print (SimplifyuseMySQL.select_datas_column(datas,6))
#[1,2,3,4]

#插入
SQL = "INSERT INTO temptest (cpu,gpu,error,wendu,shidu,times) VALUES ('{cpu}','{gpu}','{error}','{wendu}','{shidu}','{shijian}')".format(cpu = cpu ,gpu = gpu,error = pressure ,wendu = temperature,shidu = humidity,shijian = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

SimplifyuseMySQL.execute_to_mysql(SQL)
```
