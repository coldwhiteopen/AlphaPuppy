from wlkata_mirobot import WlkataMirobot, WlkataMirobotTool

import time
# 创建机械臂
arm = WlkataMirobot()
# Homing
arm.home()

#设置默认运动速度
arm.set_speed(2000)

#设置末端工具
arm.set_tool_type(WlkataMirobotTool.SUCTION_CUP)

#吸棋
def chesson():
    # 气泵开启-吸气
    arm.pump_suction()

#放棋
def chessdown():
    # 气泵关闭
    arm.pump_off()
    
#坐标变化
def xy2XY(x, y):
    if y == 8 :
        if x == 0 or x == 1 or x == 2 or x == 5 or x == 7 or x == 8 :
           print("超出范围")
        else:
            X = 1.5275*x + 19.7374*y + 102.6229
            X = round(X,1)
            Y = -20.9127*x + 1.1307*y + 88.8699
            Y = round(Y,1)
    else:
        X = 1.5275*x + 19.7374*y + 102.6229
        X = round(X,1)
        Y = -20.9127*x + 1.1307*y + 88.8699
        Y = round(Y,1)
    return X , Y


#到指定坐标
def play(X, Y):
    #初始化
    arm.go_to_zero()
    #取棋
    arm.p2p_interpolation(0, 215, 45)
    chesson()
    time.sleep(2)
    arm.go_to_zero()
    
    #放棋
    arm.p2p_interpolation(X, Y, 15)
    time.sleep(1)
    arm.p2p_interpolation(X, Y, 5)
    chessdown()
    arm.p2p_interpolation(X, Y, 15)
    arm.go_to_zero()
    
if __name__ == "__main__":
    a = 1
    X1 , Y1 = xy2XY(4,3)
    play(X1,Y1)
    time.sleep(a)
    
    X2 , Y2 = xy2XY(4,4)
    play(X2,Y2)
    time.sleep(a)
    
    X3 , Y3 = xy2XY(2,3)
    play(X3,Y3)
    time.sleep(a)
    
    X4 , Y4 = xy2XY(3,3)
    play(X4,Y4)
    time.sleep(a)
    
    X5 , Y5 = xy2XY(5,3)
    play(X5,Y5)
    time.sleep(a)
    
    X6 , Y6 = xy2XY(5,5)
    play(X6,Y6)
    time.sleep(a)
    
    X7 , Y7 = xy2XY(2,2)
    play(X7,Y7)
    time.sleep(a)
    
    X8 , Y8 = xy2XY(5,4)
    play(X8,Y8)
    time.sleep(a)
    
    X9 , Y9 = xy2XY(2,4)
    play(X9,Y9)
    time.sleep(a)
    
    X10 , Y10 = xy2XY(2,1)
    play(X10,Y10)
    time.sleep(a)
    
    X11 , Y11 = xy2XY(1,5)
    play(X11,Y11)
    time.sleep(a)
    
    X12 , Y12 = xy2XY(5,1)
    play(X12,Y12)
    time.sleep(a)
    
    X13 , Y13 = xy2XY(4,2)
    play(X13,Y13)
    time.sleep(a)