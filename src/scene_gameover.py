#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
from pygame.locals import *
# Engine
from Core.funciones import *
from Core.scene import *
from config import *
# Juego
from scene_highscores import *


# Clases
# ---------------------------------------------------------------------
class SceneOver(Scene):
    """Escena de GameOver, aqui es donde termina el juego
    y regresa al menu."""
    def __init__(self,director):
        Scene.__init__(self, director)
        # Carga la imagen.
        self.image = load_image(LOGOS + 'gameover.png')
        # Para establecer transparencia.
        self.img_alpha = 0
        # Estado de la animacion de transparencia.
        self.img_state = 0
        
    def on_update(self):
        self.time = self.director.time
    
    def on_event(self):
        # Enter para acelerar animacion.
        if self.director.key[K_RETURN] and self.img_state == 0:
            if self.director.oldkey[K_RETURN] != self.director.key[K_RETURN]:
                self.img_state = 1
                self.image.set_alpha(255)
        # Si apreta Enter pasa a la siguiente escena.
        elif self.director.key[K_RETURN] and self.img_state == 1:
            if self.director.oldkey[K_RETURN] != self.director.key[K_RETURN]:
                self.director.change_scene(SceneHighScores(self.director))
    
    def on_draw(self,screen):
        # 0 - Incremento de transparencia.
        if self.img_state == 0 and self.img_alpha < 255:
            self.img_alpha += 2
            self.image.set_alpha(self.img_alpha)
            if self.img_alpha >= 255:
                self.img_state = 1
        # 1 - Disminuye transparencia.
        if self.img_state == 1 and self.img_alpha > 0:
            self.img_alpha -= 2
            self.image.set_alpha(self.img_alpha)
            if self.img_alpha == 0:
                # Cambia a la escena menu.
                self.director.change_scene(SceneHighScores(self.director))
        # Limpia pantalla.
        screen.fill(0x000000)
        # Imprime imagen.
        screen.blit(self.image,(WIDTH/2-300,HEIGHT/2-300))
# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()