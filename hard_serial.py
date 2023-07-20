# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:02:43 2023

@author: 18444
"""

import serial
import time
# 与Arduino连接的串口端口号
serial_port = 'COM6'

# 初始化串口连接
ser = serial.Serial(serial_port, 9600, timeout=5)
time.sleep(2)
response = ser.readline().decode('utf-8')
time.sleep(0.5)
print(response)
ser.write(b'9')
response = ser.readline().decode('utf-8')
time.sleep(0.5)
print(response)
# 关闭串口连接
ser.close()