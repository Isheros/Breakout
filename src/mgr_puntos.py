#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Engine
from Core.funciones import *
from pygame.locals import *

# Clases
# ---------------------------------------------------------------------
class Puntos:
    def __init__(self):
        self.puntos = 0
        
    # Obtiene el total de puntos
    def getPuntos(self):
        return self.puntos
    
    # Agrega puntos
    def addPuntos(self,add):
        self.puntos += add
    
    # Resta Puntos
    def resPuntos(self,res):
        self.puntos -= res
        
    # Dibuja en pantalla el total de Puntos
    def draw(self,screen):
        gameprint('Puntuación:   ' + str(self.puntos),WIDTH/2+100,2,screen,False)
# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()