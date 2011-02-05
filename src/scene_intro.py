#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Engine
from Core.funciones import *
from Core.scene import *
from pygame.locals import *
from config import *

# Juego
from scene_menu import*

# Clases
# ---------------------------------------------------------------------
class SceneIntro(Scene):
    def __init__(self,director):
        Scene.__init__(self, director)
        #Carga las imagenes
        self.image1 = load_image(LOGOS + 'pygame_logo.png')
        self.image2 = load_image(LOGOS + 'lalala_logo.png')
        self.img = 0
        #Para establecer transparencia
        self.img_alpha = 0
        #Estado de la animacion de transparencia  
        self.img_state = 0
    
    def on_update(self):
        self.time = self.director.time
    
    def on_event(self):
        #Si apreta z cambia a la siguiente imagen
        if self.director.key[pygame.K_RETURN] and self.img < 2:
            if self.director.oldkey[pygame.K_RETURN] != self.director.key[pygame.K_RETURN]:
                self.img += 1
                self.img_state = 0
                self.img_alpha = 0
        #Si apreta z y ya pasaron todas las imagenes pasa a la siguiente escena
        if self.director.key[pygame.K_RETURN] and self.img == 2:
            if self.director.oldkey[pygame.K_RETURN] != self.director.key[pygame.K_RETURN]:
                self.director.change_scene(SceneMenu(self.director))

    def on_draw(self,screen):
        #Transparencia de la imagen 1
        if self.img == 0:
            # 0 - Incremento de transparencia
            if self.img_state == 0 and self.img_alpha < 255:
                self.img_alpha += 2
                self.image1.set_alpha(self.img_alpha)
                if self.img_alpha >= 255:
                    self.img_state = 1
            # 1 - Disminuye transparencia
            if self.img_state == 1 and self.img_alpha > 0:
                self.img_alpha -= 2
                self.image1.set_alpha(self.img_alpha)
                if self.img_alpha == 0:
                    self.img_state = 0
                    self.img = 1
            #Borra pantalla e imprime imagen
            screen.fill(0x000000)
            screen.blit(self.image1,(WIDTH/2-300,HEIGHT/2-300))
            
        #Transparencia de la imagen 1
        if self.img == 1:
            # 0 - Incremento de transparencia
            if self.img_state == 0 and self.img_alpha < 255:
                self.img_alpha += 2
                self.image2.set_alpha(self.img_alpha)
                if self.img_alpha >= 255:
                    self.img_state = 1
            # 1 - Disminuye transparencia
            if self.img_state == 1 and self.img_alpha > 0:
                self.img_alpha -= 2
                self.image2.set_alpha(self.img_alpha)
                if self.img_alpha == 0:
                    self.img_state = 0
                    self.director.change_scene(SceneMenu(self.director))
            #Borra pantalla e imprime imagen
            screen.fill(0x000000)
            screen.blit(self.image2,(WIDTH/2-300,HEIGHT/2-300))
# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()    