#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Engine
from Core.funciones import *
from Core.sprite import *
from pygame.locals import *

# Clases
# ---------------------------------------------------------------------
class Pad(Sprites):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(SPRITES + "pad.png", True)
        self.rect = self.image.get_rect()
        self.check_collision = True
        self.rect.x = WIDTH/2 - 30
        self.rect.y = 640
        self.speed = 0.5
        
    def onCollide(self,object):
        self.setToPreviusPosition()
        
    def setDir(self,dir,time):
        if dir == 1:
            self.rect.x -= self.speed*time
        elif dir == 2:
            self.rect.x += self.speed*time
    
    def update(self,time):
        if self.rect.x <= 0:
            self.rect.left = 0
        elif self.rect.x >= WIDTH-self.getWidth():
            self.rect.x = WIDTH-self.getWidth()
        
        self.oldPosY = self.getPosY()
        self.oldPosX = self.getPosX()
# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()