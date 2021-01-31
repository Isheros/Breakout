#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
from pygame.locals import *
# Engine
from Core.funciones import *
from Core.scene import *
from config import *
# Juego
from scene_menu import *

class SceneIntro(Scene):
    """Escena de introduccion, maneja las transicion de
    las imagenes de introduccion."""
    def __init__(self, director):
        Scene.__init__(self, director)
        # Carga las imagenes.
        self.image1 = load_image(str(LOGOS / 'pygame_logo.png'))
        self.image2 = load_image(str(LOGOS / 'lalala_logo.png'))
        self.img = 0
        # Para establecer transparencia.
        self.img_alpha = 0
        # Estado de la animacion de transparencia.
        self.img_state = 0
    
    def on_update(self):
        self.time = self.director.time
    
    def on_event(self):
        # Si apreta Enter cambia a la siguiente imagen.
        if (self.director.key[K_RETURN] and self.img < 2) and \
        self.director.oldkey[K_RETURN] != self.director.key[K_RETURN]:
            self.img += 1
            self.img_state = 0
            self.img_alpha = 0
        # Si apreta Enter y ya pasaron todas las imagenes pasa a la siguiente escena.
        if (self.director.key[K_RETURN] and self.img == 2) and \
        self.director.oldkey[K_RETURN] != self.director.key[K_RETURN]:
            self.director.change_scene(SceneMenu(self.director))

    def on_draw(self,screen):
        # Limpia la pantalla.
        screen.fill(0x000000)
        # Transparencia de la imagen 1.
        if self.img == 0:
            # 0 - Incremento de transparencia.
            if self.img_state == 0 and self.img_alpha < 255:
                self.img_alpha += 2
                self.image1.set_alpha(self.img_alpha)
                if self.img_alpha >= 255:
                    self.img_state = 1
            # 1 - Disminuye transparencia.
            if self.img_state == 1 and self.img_alpha > 0:
                self.img_alpha -= 2
                self.image1.set_alpha(self.img_alpha)
                if self.img_alpha == 0:
                    self.img_state = 0
                    self.img = 1
            # Imprime la imagen.
            screen.blit(self.image1,(WIDTH/2-300,HEIGHT/2-300))
            
        # Transparencia de la imagen 2.
        if self.img == 1:
            # 0 - Incremento de transparencia.
            if self.img_state == 0 and self.img_alpha < 255:
                self.img_alpha += 2
                self.image2.set_alpha(self.img_alpha)
                if self.img_alpha >= 255:
                    self.img_state = 1
            # 1 - Disminuye transparencia.
            if self.img_state == 1 and self.img_alpha > 0:
                self.img_alpha -= 2
                self.image2.set_alpha(self.img_alpha)
                if self.img_alpha == 0:
                    self.img_state = 0
                    self.director.change_scene(SceneMenu(self.director))
            # Imprime la imagen.
            screen.blit(self.image2,(WIDTH/2-300,HEIGHT/2-300))