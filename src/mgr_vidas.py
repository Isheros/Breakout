#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
from pygame.locals import *
# Engine
from Core.funciones import *

# Clases
# ---------------------------------------------------------------------
class Vidas:
    """Maneja las vidas."""
    def __init__(self):
        self.vidas = 3
    
    def setVidas(self,vidas):
        """Establece las vidas."""
        self.vidas = vidas
        
    def getVidas(self):
        """Devuelve cuantas vidas hay."""
        return self.vidas
    
    def addVidas(self):
        """Agrega una vida."""
        self.vidas += 1
        
    def resVidas(self):
        """Resta una vida."""
        self.vidas -= 1
        
    def draw(self,screen):
        """Dibuja en pantalla cuantas vidas quedan."""
        gameprint('Vidas:   ' + str(self.vidas),WIDTH/2-200,2,screen,False)
# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()