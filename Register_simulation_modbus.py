import asyncio
import traceback
from time import localtime, sleep, strftime, time

import modbus_tk.defines as cst
from faker import Faker
from modbus_tk import modbus_tcp

import config_modbus as con
import MySQLuse.SimplifyuseMySQL as mysql

fake = Faker('zh_CN')

async def getdatafrom_redis(delay, slave_num,regs_dic,ranges): 
    try:
        await asyncio.sleep(delay)
        for regs in regs_dic:
            if regs_dic[regs]["mode"] == '1':
                master.execute(slave_num, cst.WRITE_MULTIPLE_REGISTERS, int(regs-400001), 
                output_value=[float(fake.random_int(min = int((regs_dic[regs]["min"])*100),max = int((regs_dic[regs]["max"])*100))/100 )], data_format='>f'
                )
            elif regs_dic[regs]["mode"] == '2':
                master.execute(slave_num, cst.WRITE_MULTIPLE_REGISTERS, int(regs-400001), 
                output_value=[float( float(regs_dic[regs]["min"]) + ranges*(float(regs_dic[regs]["max"]))  )], data_format='>f'
                )
    except BaseException as e:
        print(traceback.format_exc())
ranges = 0

while True:
    regs_dic = {}
    for tup in mysql.select_MYSQL("SELECT regs,min,max,mode FROM simulation_test ORDER BY regs"):
        regs_dic.update({tup[0]:{"mode":tup[3],"min":tup[1],"max":tup[2]}})

    master = modbus_tcp.TcpMaster(host='127.0.0.1',port=5566)
    async def main():
            astime = time()
            for i in range(con.div_num):
                    await asyncio.create_task(getdatafrom_redis(0, i+1,regs_dic,ranges))
            aetime = time()
            print('all-time',aetime-astime)
    asyncio.run(main())
    ranges = ranges+1
    sleep(5)