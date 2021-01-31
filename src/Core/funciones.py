#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pickle
from pathlib import Path
# Pygame
import pygame
from pygame.locals import *
# Engine
from config import *

# Carga Imagenes
def load_image(name, transparent=False):
    """Facilita el cargado de imagenes."""
    print(name)
    image = pygame.image.load(name).convert()
    if transparent:
        color = image.get_at((0, 0))
        image.set_colorkey(color, 0)
    return image

# Texto
def gameprint(text, posx, posy, screen, shadow=True, font=F_COMFORTAA,
              color1=(255, 255, 255), color2=(155,155,155)):
    """Facilita el imprimir texto.
    (Texto,PosX,PosY,Superficie,Sombra,Fuente,Color,ColorSombra)"""
    font = pygame.font.Font(font, 16)
    ren = font.render(text, 1, color1)
    ren_shadow = font.render(text, 1, color2)
    if shadow:
        screen.blit(ren_shadow,(posx + 2, posy + 2))
    screen.blit(ren, (posx, posy))

# Colisiones
def checkCollision(object1, object2):
    """Chequea colisiones."""
    
    if object1.getCheckCollision() and object2.getCheckCollision():
        x1 = object1.getPosX()
        w1 = object1.getWidth()
        y1 = object1.getPosY()
        h1 = object1.getHeight()
        
        x2 = object2.getPosX()
        w2 = object2.getWidth()
        y2 = object2.getPosY()
        h2 = object2.getHeight()
        
        if (((x1 <= x2+w2+.5 and x1 > x2) or (x2 <= x1+w1+.5 and x2 > x1)) and
            ((y1 <= y2+h2+.5 and y1 > y2) or (y2 <= y1+h1+.5 and y2 > y1))):
            return True
    return False

# Carga objetos
def loadFile(filename):
    """Carga archivos externos."""
    archivo = open(filename, 'rb')
    fileloaded = pickle.load(archivo)
    archivo.close()
    return fileloaded

# Salva objetos
def saveFile(filename, var):
    """Guarda archivos externos."""
    archivo = open(filename, 'wb')
    pickle.dump(var, archivo)
    archivo.close()