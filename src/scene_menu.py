#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
from pygame.locals import *
# Engine
from Core.funciones import *
from Core.scene import *
from Core.menu import *
from config import *
# Juego
from scene_game import *
from scene_highscores import *


# Clases
# ---------------------------------------------------------------------
class SceneMenu(Scene):
    def __init__(self, director):
        Scene.__init__(self, director)
        # Carga las imagenes.
        self.frame = load_image(FRAMEWORK+"frame.png", True)
        self.background = load_image(LOGOS+"breakout_logo.png")
        # Funciones del menu.
        def comenzar_juego():
            director.change_scene(SceneGame(director))
        def puntajes():
            director.change_scene(SceneHighScores(director))
        def mostrar_opciones():
            archivo = open('Data\data.pkg', 'r')
            puntajes = cPickle.load(archivo)
            archivo.close()
            print str(puntajes)
        def salir_del_programa():
            director.quit()
        # Menu.
        self.opciones = [
        ("Jugar", comenzar_juego),
        ("Puntuaciones", puntajes),
        ("Opciones", mostrar_opciones),
        ("Salir", salir_del_programa)]
        # Carga menu.
        self.menu = Menu(self.opciones,WIDTH/2 - 90,HEIGHT/2 - 55)

    def on_update(self):
        self.time = self.director.time
        
    def on_event(self):
        self.menu.update(self.director.key,self.director.oldkey)

    def on_draw(self, screen):
        # Borra la pantalla e imprime Background
        screen.fill(0x000000)
        screen.blit(self.background,(WIDTH/2 - 300,HEIGHT/2-300))
        # Imprime el frame
        screen.blit(self.frame,(WIDTH/2-103,HEIGHT/2-61))
        # Imprime menu
        self.menu.draw(screen)

# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()