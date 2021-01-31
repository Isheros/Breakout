#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
import pygame
from pygame.locals import *
# Engine
from Core.funciones import *

class Sprites(pygame.sprite.Sprite):
    """Representa a los sprites del juego."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.check_collision = True
        
    def getHeight(self):
        """Devuelve la altura del sprite."""
        return self.rect.height
    
    def getWidth(self):
        """Devuelve el ancho del sprite."""
        return self.rect.width
        
    def setPos(self,x,y):
        """Establece la posicion del sprite(PosX,PosY)."""
        self.rect.x = x
        self.rect.y = y
        
    def getPosX(self):
        """Devuelve la posicion X del sprite."""
        return self.rect.x
    
    def getPosY(self):
        """Devuelve la posicion Y del sprite."""
        return self.rect.y
    
    def setToPreviusPosition(self):
        """Coloca al sprite en la posicion que ocupaba
        en la ultima iteracion."""
        self.setPos(self.oldPosX,self.oldPosY)
    
    def setCheckCollision(self,check):
        """Establece si puede colisionar."""
        self.check_collision = check
        
    def getCheckCollision(self):
        """Obtiene si el sprite es colisionable."""
        return self.check_collision
    
    def draw(self,screen):
        """Dibuja al sprite en pantalla."""
        screen.blit(self.image,(self.getPosX(),self.getPosY()))