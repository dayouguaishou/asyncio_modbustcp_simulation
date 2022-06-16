import asyncio
import traceback

import modbus_tk.defines as cst
from modbus_tk import modbus_tcp

import config_modbus as con


async def getdatafrom_redis(delay, slave_num): 
    try:
        await asyncio.sleep(delay)
        SLAVE1 = SERVER.add_slave(slave_num)
        #SLAVE1.add_block('01', cst.READ_COILS, 0, con.rig_num_E)
        SLAVE1.add_block('03', cst.HOLDING_REGISTERS,con.rig_num_S,con.rig_num_E)
    except BaseException as e:
        print(traceback.format_exc())


SERVER = modbus_tcp.TcpServer(address="0.0.0.0", port=5566) 
SERVER.start()
async def main():
    for i in range(con.div_num):

        await asyncio.create_task(getdatafrom_redis(0, i+1))

asyncio.run(main())
