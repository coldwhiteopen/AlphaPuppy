# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 14:51:56 2023

@author: Phydr0
"""

"""
    使用python实现：读取USB摄像头的画面
"""
# 导入CV2模块
import cv2
import numpy as np
import time

def rotation(src, angle=0, scale=1.0):
    rows, cols = src.shape[:2]
    center = (cols // 2, rows // 2)
    rotMat = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(src, rotMat, (cols, rows))
    return rotated

def get_board(src):
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=3)
    
    mask = cv2.bitwise_not(mask)
    contours,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contours.sort(key=lambda c: cv2.contourArea(c), reverse=True)
    # print(contours[0])
    minp = [240, 320]
    maxp = [240, 320]
    for point in contours[0]:
        point = point[0]
        if point[0] < minp[0]:
            minp[0] = point[0]
        if point[1] < minp[1]:
            minp[1] = point[1]
        if point[0] > maxp[0]:
            maxp[0] = point[0]
        if point[1] > maxp[1]:
            maxp[1] = point[1]
    print(maxp, minp)
    width = round((maxp[1] - minp[1])/8)
    height = round((maxp[0] - minp[0])/8)
    img = np.zeros((480, 640), np.uint8)
    mask=cv2.drawContours(img,contours,0,255,cv2.FILLED)
    cv2.imshow('mask',mask)
    red_pixel = cv2.bitwise_and(src, src, mask=mask)
    cv2.imshow('red',red_pixel)
    
    board_now = np.zeros((8,8))
    
    '''找出黑棋位置'''
    lower_b = np.array([0, 0, 0])
    upper_b = np.array([180, 255, 46])
    black = cv2.inRange(hsv, lower_b, upper_b)
    kernel = np.ones((10, 10), np.uint8)
    black = cv2.erode(black, kernel)
    
    b_contours,hierarchy=cv2.findContours(black,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for contour in b_contours:
        M = cv2.moments(contour)
        if M['m00'] == 0:
            continue
        Cx = int(M['m10']/M['m00'])
        Cy = int(M['m01']/M['m00'])
        print(Cx,Cy)
        if Cx < minp[1] - 10 or Cx > maxp[1] + 10 or Cy < minp[0] - 10 or Cy > maxp[0] + 10:
            continue
        x = round((Cx - minp[1])/width)
        y = round((Cy - minp[0])/height)
        if x<8 and y<8:
            board_now[y][x] = 1
        else:
            print('请正确摆放棋子')
            
    '''找出白棋位置'''
    lower_w = np.array([90, 5, 166])
    upper_w = np.array([117, 56, 255])
    white = cv2.inRange(hsv, lower_w, upper_w)
    kernel = np.ones((5, 5), np.uint8)
    white = cv2.erode(white, kernel)
    
    w_contours,hierarchy=cv2.findContours(white,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for contour in w_contours:
        M = cv2.moments(contour)
        if M['m00'] == 0:
            continue
        Cx = int(M['m10']/M['m00'])
        Cy = int(M['m01']/M['m00'])
        print(Cx,Cy)
        if Cx < minp[1] - 10 or Cx > maxp[1] + 10 or Cy < minp[0] - 10 or Cy > maxp[0] + 10:
            continue
        x = round((Cx - minp[1])/width)
        y = round((Cy - minp[0])/height)
        if x<8 and y<8:
            board_now[y][x] = -1
        else:
            print('请正确摆放棋子')
    
    print(board_now)
    cv2.imshow('black', black)
    cv2.imshow('white', white)
    return board_now
    

def get_red_pixel(src):
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=3)
    
    mask = cv2.bitwise_not(mask)
    
    cv2.imshow('mask',mask)
    red_pixel = cv2.bitwise_and(src, src, mask=mask)
    cv2.imshow('red',red_pixel)
    return red_pixel

def get_rect_point(src):
    red_pixel = get_red_pixel(src)
    gray = cv2.cvtColor(red_pixel, cv2.COLOR_BGR2GRAY)

    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours_poly = [cv2.approxPolyDP(contour, 80, True) for contour in contours]
    contours_poly.sort(key=cv2.contourArea, reverse=True)

    if len(contours_poly) < 1 or len(contours_poly[0]) != 4:
        return False, None

    outer = contours_poly[0]
    if (outer[0][0][0] + outer[0][0][1]) < (outer[1][0][0] + outer[1][0][1]):
        rect_point = outer[:4]
    else:
        rect_point = [outer[1], outer[2], outer[3], outer[0]]

    return True, rect_point

def warp(src, rect_point):
    rect_point2 = np.float32([[0, 0], [0, src.shape[0]], [src.shape[1], src.shape[0]], [src.shape[1], 0]])
    element_transf = cv2.getPerspectiveTransform(np.float32(rect_point), rect_point2)
    warped = cv2.warpPerspective(src, element_transf, (src.shape[1], src.shape[0]))
    return warped

def image_processor(src):
    src = rotation(src)
    src = cv2.GaussianBlur(src, (3, 3), 0)

    success, rect_point = get_rect_point(src)
    if not success:
        return False, src

    src = warp(src, rect_point)
    return True, src

def read_usb_capture():
    # 选择摄像头的编号
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    # 添加这句是可以用鼠标拖动弹出的窗体
    cv2.namedWindow('real_img', cv2.WINDOW_NORMAL)
    
    shot = 0
    
    while(cap.isOpened()):
        # 读取摄像头的画面
        ret, frame = cap.read()
        # 真实图
        cv2.imshow('real_img', frame)
        shot += 1
        if shot%10 == 0:
            t = time.perf_counter()
            get_board(frame)
            print(f'coast:{time.perf_counter() - t:.8f}s')
        
        # 按下'q'就退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # 释放画面
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    read_usb_capture()
