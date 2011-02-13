#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
from pygame.locals import *
# Engine
from Core.funciones import *

# Clases
# ---------------------------------------------------------------------
class Puntos:
    """Maneja los puntos."""
    def __init__(self):
        self.puntos = 0
        
    def getPuntos(self):
        """Obtiene el cuantos puntos llevas."""
        return self.puntos
    
    def addPuntos(self,add):
        """Añade puntos al score."""
        self.puntos += add
    
    def resPuntos(self,res):
        """Resta puntos del score."""
        self.puntos -= res
        
    def draw(self,screen):
        """Dibuja en pantalla tu score."""
        gameprint('Puntuación:   ' + str(self.puntos),WIDTH/2+100,2,screen,False)
# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()