#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame
import sys

from pygame.locals import *
from funciones import *

# Clases
# ---------------------------------------------------------------------

class Sprites(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.check_collision = True
        
    def getHeight(self):
        return self.rect.height
    
    def getWidth(self):
        return self.rect.width
        
    def setPos(self,x,y):
        self.rect.x = x
        self.rect.y = y
        
    def getPosX(self):
        return self.rect.x
    
    def getPosY(self):
        return self.rect.y
    
    def setToPreviusPosition(self):
        self.setPos(self.oldPosX,self.oldPosY)
    
    def setCheckCollision(self,check):
        self.check_collision = check
        
    def getCheckCollision(self):
        return self.check_collision
    
    def draw(self,screen):
        screen.blit(self.image,(self.getPosX(),self.getPosY()))
# ---------------------------------------------------------------------
def main():
    return 0

if __name__ == '__main__':
    main()