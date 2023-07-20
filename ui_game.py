# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 08:17:28 2023

@author: Phydr0
"""

import pygame
import sys
import game

from mcts_pure import MCTSPlayer as MCTS_Pure
from mcts_alphaZero import MCTSPlayer
from policy_value_net_numpy import PolicyValueNetNumpy

from pygame.locals import QUIT,KEYDOWN

pygame.init()

screen = pygame.display.set_mode((670,670))
screen_color = [238,154,73]
line_color = [255,255,255]

def find_pos(x,y):
    for i in range(69,670,76):
        for j in range(69,670,76):
            L1=i-38
            L2=i+38
            R1=j-38
            R2=j+38
            if x>=L1 and x<=L2 and y>=R1 and y<=R2:
                return i,j
    return x,y

def check_over_pos(x,y,over_pos):
    for val in over_pos:
        if val[0][0]==x and val[0][1]==y:
            return False
    return True


def run():
    
    flag=False
    tim=0

    over_pos = []
    white = [255,255,255]
    black = [0,0,0]
    
    while True:
        for event in pygame.event.get():
            if event.type in (QUIT,KEYDOWN):
                sys.exit()
        screen.fill(screen_color)
        for i in range(69,670,76):
            if i==69 or i==670-69:
                pygame.draw.line(screen,line_color,[i,69],[i,670-69],4)
                pygame.draw.line(screen,line_color,[69,i],[670-69,i],4)
            else:
                pygame.draw.line(screen,line_color,[i,69],[i,670-69],2)
                pygame.draw.line(screen,line_color,[69,i],[670-69,i],2)
            
        for val in over_pos:
            pygame.draw.circle(screen, val[1],val[0], 36,0)
            
        x,y = pygame.mouse.get_pos()
        
        if x<32 or y<32 or x>638 or y>638:
            pygame.display.update()
            continue
        
        
        '''绘制鼠标位置附近落棋点的方框'''
        x,y = find_pos(x, y)
        if check_over_pos(x, y, over_pos):
            pygame.draw.rect(screen,[0,154,214],[x-38,y-38,76,76],2,1)
            
        keys_pressed = pygame.mouse.get_pressed()
        
        
        '''点击将当前落棋位置存储'''
        if keys_pressed[0] and tim==0:
            flag=True
            if check_over_pos(x, y, over_pos):
                if len(over_pos)%2==0:
                    over_pos.append([[x,y],black])
                else:
                    over_pos.append([[x,y],white])
               
        '''鼠标点击延时，防止连续点击'''
        if flag:
            tim+=1
        if tim%200==0:
            flag=False
            tim=0
            
        pygame.display.update()
    

if __name__ == '__main__':
    run()




