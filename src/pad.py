#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
from pygame.locals import *
# Engine
from Core.funciones import *
from Core.sprite import *

class Pad(Sprites):
    """La clase del pad, maneja los movimientos y colisiones
    del pad."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(SPRITES/"pad.png", True)
        self.rect = self.image.get_rect()
        self.check_collision = True
        self.rect.x = WIDTH/2 - 30
        self.rect.y = 640
        self.speed = 0.5
        
    def onCollide(self,object):
        pass
        
    def setDir(self,dir,time):
        """Establece la direccion del pad."""
        if dir == 1:
            self.rect.x -= self.speed*time
        elif dir == 2:
            self.rect.x += self.speed*time
    
    def update(self,time):
        """Actualiza el pad."""
        if self.rect.x <= 0:
            self.rect.left = 0
        elif self.rect.x >= WIDTH-self.getWidth():
            self.rect.x = WIDTH-self.getWidth()
        
        # Actualiza la posicion anterior.
        self.oldPosY = self.getPosY()
        self.oldPosX = self.getPosX()