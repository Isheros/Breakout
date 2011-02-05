#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Engine
from Core.funciones import *
from Core.sprite import *
from pygame.locals import *

# Módulos
import math

# Clases
# ---------------------------------------------------------------------
class Ball(Sprites):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(SPRITES + "ball.png",True)
        self.rect = self.image.get_rect()
        self.check_collision = True
        #Velocidad Inicial
        self.speed = [0.4,-0.4]
        #Al inicio estara pegada al pad
        self.is_sticky = True
        self.resVida = False
        self.addPuntos = False
        
    def setSticky(self,is_sticky):
        self.is_sticky = is_sticky
    
    def getSticky(self):
        return self.is_sticky
    
    def onCollide(self,object):
        self.setToPreviusPosition()
        # Colision con la parte izquierda
        if self.rect.centerx <= object.rect.centerx:
            dist = object.rect.centerx - self.rect.centerx
            self.speed[0] = -math.sin(math.radians(dist))/1.20
        # Colision con la parte derecha
        elif self.rect.centerx > object.rect.centerx:
            dist = self.rect.centerx - object.rect.centerx
            self.speed[0] = math.sin(math.radians(dist))/1.20
        self.speed[1] = -self.speed[1]
        
    def onCollideBrick(self,object):
        self.setToPreviusPosition()
        self.addPuntos = True
        # Borde izquierdo
        if self.getPosX() <= object.getPosX()+object.getWidth():
            self.speed[1] = -self.speed[1]
        # Borde derecho
        elif self.getPosX()+self.getWidth() >= object.getPosX():
            self.speed[1] = -self.speed[1]
        # Borde superior
        elif self.getPosY() <= object.getPosY()+object.getHeight():
            self.speed[0] = -self.speed[0]
        # Borde inferior
        elif self.getPosY()+self.getHeight() >= object.getPosY():
            self.speed[0] = -self.speed[0]
        
    def update(self,time):
        # Actualiza la posicion de la bola
        self.rect.x += self.speed[0] * time
        self.rect.y += self.speed[1] * time
        
        # Verifica si choca con el borde izquierdo
        if self.rect.left <= 0:
            self.rect.left = 0
            self.speed[0] = -self.speed[0]
        # Verifica si choca con el borde derecho
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.speed[0] = -self.speed[0]
        # Verifica si choca con el borde superior
        if self.rect.top <= 0:
            self.rect.top = 0
            self.speed[1] = -self.speed[1]
        # Borde inferior
        if self.rect.bottom >= HEIGHT:
            self.resVida = True
            self.setSticky(True)
            
        self.oldPosY = self.getPosY()
        self.oldPosX = self.getPosX()
# ---------------------------------------------------------------------
def main():
    return 0

if __name__ == '__main__':
    main()