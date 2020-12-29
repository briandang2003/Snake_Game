import math
import random 
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0 
    w = 0 
    def _init_self(self, start, dirnx=1, dirny=0,color=(255,0,0)):
        pass

    def move(self,dirnx, dirny):
        pass
    def draw (self, surface, eyes=False):
        pass

class snake(object):
    def _init_ (self,color,pos):
        pass

    def move(self):
        pass
    def reset(self,pos):
        pass

    def addCube(self):
        pass
    def draw(self, surface):
        pass

    
def drawGrid(w, rows, surface):
    # figure cap between lines 
    sizeBtwn = w // rows
 
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
 
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))
    pass

def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill(0,0,0)
    drawGrid(width, rows, surface)
    pygame.display.update()


def main():
    global width, rows
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width,height))
    s = snake((250,0,0)) , (10,10)
    flag = True
    clock = pygame.time.Clock()

    while flag: 
        pygame.time.delay( 50)
        clock.tick(10)
        # make sure the game doesn't run more than 10 frames per sec
        # delay by a few mili sec 
        # the lower the delay is the faster the game will be
        # the lower tick goes the slower it will be 

        redrawWindow(win) 
        #haven't been coded yet




    pass 

# rows = 
# w = 
# h = 
# cube.w = w
# main()

