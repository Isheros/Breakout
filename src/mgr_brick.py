#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
from pygame.locals import *
# Engine
from Core.funciones import *
# Juego
from brick import *

# Constantes
BRICKS_PER_SIDE = 10
BRICKS_FILES = 6
START_POS_X = 5
START_POS_Y = 100

# Clases
# ---------------------------------------------------------------------
class BrickMgr():
    def __init__(self):
        self.brick=[]
        for y in range(BRICKS_FILES):
            for x in range(BRICKS_PER_SIDE):
            
                self.brick.append(Brick())
                
                w = self.brick[y*BRICKS_PER_SIDE+x].getWidth()
                h = self.brick[y*BRICKS_PER_SIDE+x].getHeight()
                
                self.brick[y*BRICKS_PER_SIDE+x].setPos(START_POS_X+x*(w-1),START_POS_Y+y*(h-1))
                
    def update(self,ball):
        for y in range(BRICKS_FILES):
            for x in range(BRICKS_PER_SIDE):
                self.brick[y*BRICKS_PER_SIDE+x].update
                
                if checkCollision(ball,self.brick[y*BRICKS_PER_SIDE+x]):
                    ball.onCollideBrick(self.brick[y*BRICKS_PER_SIDE+x])
                    self.brick[y*BRICKS_PER_SIDE+x].onCollide(ball)
                    
                    
    def draw(self,screen):
        for y in range(BRICKS_FILES):
            for x in range(BRICKS_PER_SIDE):
                self.brick[y*BRICKS_PER_SIDE+x].draw(screen)
                
# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()