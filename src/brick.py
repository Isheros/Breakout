#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
from pygame.locals import *
# Engine
from Core.funciones import *
from Core.sprite import *

# Clases
# ---------------------------------------------------------------------
class Brick(Sprites):
    """Maneja el comportamiento del ladrillo."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(SPRITES+"brick.png")
        self.rect = self.image.get_rect()
        self.check_collision = True
        self.visible = True
        
    def setVisible(self,visible):
        """Establece si es visible o no."""
        self.visible = visible
        
    def onCollide(self,object):
        """Cuando colisiona lo vuelve invisible y no
        puede colisionar de nuevo."""
        self.setVisible(False)
        self.setCheckCollision(False)
        
    def draw(self,screen):
        """Dibuja en pantalla al ladrillo si este es
        visible."""
        if self.visible:
            screen.blit(self.image, self.rect)
# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()