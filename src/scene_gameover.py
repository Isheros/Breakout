#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Engine
from Core.funciones import *
from Core.scene import *
from pygame.locals import *
from config import *

# Juego
import scene_menu 


# Clases
# ---------------------------------------------------------------------
class SceneOver(Scene):
    def __init__(self,director):
        Scene.__init__(self, director)
        # Carga la imagen
        self.image = load_image(LOGOS + 'gameover.png')
        #Para establecer transparencia
        self.img_alpha = 0
        #Estado de la animacion de transparencia  
        self.img_state = 0
        
    def on_update(self):
        self.time = self.director.time
    
    def on_event(self):
        # Enter para acelerar animacion
        if self.director.key[pygame.K_RETURN] and self.img_state == 0:
            if self.director.oldkey[pygame.K_RETURN] != self.director.key[pygame.K_RETURN]:
                self.img_state = 1
                self.image.set_alpha(255)
        #Si apreta z y ya pasaron todas las imagenes pasa a la siguiente escena
        elif self.director.key[pygame.K_RETURN] and self.img_state == 1:
            if self.director.oldkey[pygame.K_RETURN] != self.director.key[pygame.K_RETURN]:
                self.director.change_scene(scene_menu.SceneMenu(self.director))
    
    def on_draw(self,screen):
        # 0 - Incremento de transparencia
        if self.img_state == 0 and self.img_alpha < 255:
            self.img_alpha += 2
            self.image.set_alpha(self.img_alpha)
            if self.img_alpha >= 255:
                self.img_state = 1
        # 1 - Disminuye transparencia
        if self.img_state == 1 and self.img_alpha > 0:
            self.img_alpha -= 2
            self.image.set_alpha(self.img_alpha)
            if self.img_alpha == 0:
                self.director.change_scene(scene_menu.SceneMenu(self.director))
        #Borra pantalla e imprime imagen
        screen.fill(0x000000)
        screen.blit(self.image,(WIDTH/2-300,HEIGHT/2-300))
# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()