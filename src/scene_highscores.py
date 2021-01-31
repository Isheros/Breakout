#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
from pygame.locals import *
# Engine
from Core.funciones import *
from Core.scene import *
from config import *
# Juego
from mgr_puntuaciones import *

from scene_gameover import *
import scene_menu

class SceneHighScores(Scene):
    """Escena de las altas puntuaciones, aqui se muestran las
    3 mejores puntuaciones."""
    def __init__(self, director):
        Scene.__init__(self, director)
        self.frame = load_image(FRAMEWORK / "frame.png", True)
        puntos = Puntuaciones()
        puntos.organize()
        self.first = puntos.first
        self.second = puntos.second
        self.third = puntos.third
        
    def on_update(self):
        self.time = self.director.time
    
    def on_event(self):
        if self.director.key[K_RETURN] and \
        self.director.oldkey[K_RETURN] != self.director.key[K_RETURN]:
            self.director.change_scene(scene_menu.SceneMenu(self.director))
    
    def on_draw(self,screen):
        # Borra la pantalla
        screen.fill(0x000000)
        # Imprime Frame
        screen.blit(self.frame,(WIDTH/2-103,HEIGHT/2-61))
        # Imprime Lugar
        gameprint('1 - Lugar:',WIDTH/2 - 88, HEIGHT/2 - 55, screen)
        gameprint('2 - Lugar:',WIDTH/2 - 90, HEIGHT/2 - 10, screen)
        gameprint('3 - Lugar:',WIDTH/2 - 90, HEIGHT/2 + 35, screen)
        # Imprime Puntuaciones
        gameprint(str(self.first),WIDTH/2 + 30, HEIGHT/2 - 55, screen)
        gameprint(str(self.second),WIDTH/2 + 30, HEIGHT/2 - 10, screen)
        gameprint(str(self.third),WIDTH/2 + 30, HEIGHT/2 + 35, screen)