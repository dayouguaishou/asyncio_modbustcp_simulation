# 利用协程实现模拟多个ModbusTcpServer 

0.导入的第三方库
----
```
pip3 install modbus_tk
```

1.模拟器配置文件
----
config_modbus.py --> ModbusTcpServer模拟器配置文件
div_num --> 模拟的设备数量
rig_num --> 每一个设备模拟的寄存器数量（03功能码，800个寄存器可模拟400个float变量）

2.设备及寄存器模拟器
----
Equipment_simulation_modbus.py --> ModbusTcpServer设备及寄存器模拟器
```
SERVER = modbus_tcp.TcpServer(address="0.0.0.0", port=5566) 
```
注意修改address及port，ModbusTcp默认port端口应为502，如果该程序运行在云服务器上，请注意修改端口号
如果在一台服务器上想运行多个ModbusTcpServer设备及寄存器模拟器，可以使用不同的端口号

3.寄存器数据刷新
----
Register_simulation_modbus.py --> ModbusTcpServer设备及寄存器更新
从mysql数据库中读取寄存器模拟的最大最小值，通过Faker库（随手拿来用的）模拟出值再写到寄存器中


效果：
----
模拟了250个ModbusTcp设备，每个设备开通了4号寄存器800个（40001 --> 40801），共20W寄存器，模拟刷新的数据每个设备大约120个float
