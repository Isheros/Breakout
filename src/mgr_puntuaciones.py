#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Engine
from Core.funciones import *
from pygame.locals import *

class Puntuaciones:
    def __init__(self,puntuacion=0):
        self.puntos = puntuacion
        self.puntuacion = loadFile('Data\data.pkg')
        # Valores
        self.values = list(self.puntuacion.values())
        self.first = self.values[0]
        self.second = self.values[1]
        self.third = self.values[2]
        
    def organize(self):
        if self.puntos >= self.first:
            self.first = self.puntos
        elif self.puntos >= self.second and self.puntos < self.first:
            self.second = self.puntos
        elif self.puntos >= self.third and self.puntos < self.second:
            self.third = self.puntos
            
    def replace(self):
        self.organize()
        self.puntuacion = {'1-Lugar': self.first,
                           '2-Lugar': self.second,
                           '3-Lugar': self.third}
        saveFile('Data\data.pkg',self.puntuacion)