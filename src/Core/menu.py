#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
from pygame.locals import *
# Engine
from funciones import *

# Clases
# ---------------------------------------------------------------------
class Opcion:
    
    def __init__(self, opcion, x, y,paridad,funcion):
        # Inicializa colores de Opcion (no implementado)
        self.color_normal = (255,255,255)
        self.color_select = (255,0,0)
        self.color_desact = (75,75,75)
        # Color de texto
        self.color = self.color_normal
        # Posicion de la opcion
        self.destinox = x
        self.rectx = 500 * paridad
        self.recty = y
        self.x = float(self.rectx)
        # Nombre de la opcion y funcion
        self.funcion = funcion
        self.opcion = opcion
        
    def update(self):
        # Trancion de Inicio
        self.x += (self.destinox - self.x) / 10.0
        self.rectx = int(self.x)

    def activar(self):
        # Activa la funcion
        self.funcion()
        
    def draw(self, screen):
        # Dibuja en pantalla la opcion
        gameprint(self.opcion,self.rectx,self.recty,screen,color1=self.color)
        
# ---------------------------------------------------------------------
class Cursor:
    
    def __init__(self, x, y, dy):
        # Imagen del cursor
        self.image = load_image(FRAMEWORK+'select.png',True)
        # Posicion del cursor
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0

    def update(self):
        # Transicion del cursor
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        # Seleccionar
        self.to_y = self.y_inicial + indice * self.dy

    def draw(self, screen):
        # Dibuja en pantalla el cursor
        screen.blit(self.image, self.rect)
        
# ---------------------------------------------------------------------
class Menu:
    
    def __init__(self, opciones,x,y):
        self.opciones = []
        self.x = x
        self.y = y
        paridad = 1
        # Inicia Cursor
        self.cursor = Cursor(x - 30, y + 5, 30)
        # Inicia las Opciones
        for titulo, funcion in opciones:
            self.opciones.append(Opcion(titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1
        self.seleccionado = 0
        self.total = len(self.opciones)

    def update(self,key,oldkey):
        # Si presiono arriba
        if key[pygame.K_UP]:
            if oldkey[pygame.K_UP] != key[pygame.K_UP]:
                self.seleccionado -= 1
        # Si presiono abajo
        elif key[pygame.K_DOWN]:
            if oldkey[pygame.K_DOWN] != key[pygame.K_DOWN]:
                self.seleccionado += 1
        # Si presiono Enter
        elif key[pygame.K_RETURN]:
            if key[pygame.K_RETURN] != oldkey[pygame.K_RETURN]:
                # Invoca a la función asociada a la opción.
                self.opciones[self.seleccionado].activar()

        # Procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        # Actualiza Cursor
        self.cursor.update()
        
        # Actualiza Opciones
        for o in self.opciones:
            o.update()

    def draw(self, screen):
        self.cursor.draw(screen)
        for opcion in self.opciones:
            opcion.draw(screen)
# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()