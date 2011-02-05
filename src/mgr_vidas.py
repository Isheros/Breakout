#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Engine
from Core.funciones import *
from pygame.locals import *

# Clases
# ---------------------------------------------------------------------
class Vidas:
    def __init__(self):
        self.vidas = 3
    
    # Establece vidas
    def setVidas(self,vidas):
        self.vidas = vidas
        
    # Retorna cuantas vidas quedan
    def getVidas(self):
        return self.vidas
    
    # Agrega una vida
    def addVidas(self):
        self.vidas += 1
    
    # Resta una vida
    def resVidas(self):
        self.vidas -= 1
        
    # Dibuja en pantalla el total de vidas
    def draw(self,screen):
        gameprint('Vidas:   ' + str(self.vidas),WIDTH/2-200,2,screen,False)
# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()