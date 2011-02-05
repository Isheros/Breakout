#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame
import sys

from pygame.locals import *
from funciones import *

# Clases
# ---------------------------------------------------------------------
class Director:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Breakout")
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()
        self.key = None
        self.oldkey = None
#----------------------------------------------------------------------
    def loop(self):
        "Pone en funcionamiento el juego."
        while not self.quit_flag:
            self.time = self.clock.tick(60)
            
            # Eventos de Salida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                        
            #Lee las teclas presionadas
            self.key = pygame.key.get_pressed()
            
            # Detecta eventos
            self.scene.on_event()
            
            # actualiza la escena
            self.scene.on_update()
            
            # dibuja la pantalla
            self.scene.on_draw(self.screen)
            pygame.display.flip()
            
            #Actualiza pulsaciones
            self.oldkey = self.key
    def change_scene(self, scene):
        "Altera la escena actual."
        self.scene = scene
        
    def quit(self):
        self.quit_flag = True
# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()
