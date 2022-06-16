from faker import Faker
import MySQLuse.SimplifyuseMySQL as mysql


#fake = Faker('zh_CN')
#print(float(fake.random_int(min = 5000,max = 5000)/100 ))

regs_dic = {}
for tup in mysql.select_MYSQL("SELECT regs,min,max,mode FROM simulation_test ORDER BY regs"):
    regs_dic.update({tup[0]:{"mode":tup[3],"min":tup[1],"max":tup[2]}})

for regs in regs_dic:
    print(regs_dic[regs])