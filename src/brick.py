#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Engine
from Core.funciones import *
from Core.sprite import *
from pygame.locals import *

# Clases
# ---------------------------------------------------------------------
class Brick(Sprites):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(SPRITES+"brick.png")
        self.rect = self.image.get_rect()
        self.check_collision = True
        self.visible = True
        
    def setVisible(self,visible):
        self.visible = visible
        
    def onCollide(self,object):
        self.setVisible(False)
        self.setCheckCollision(False)
        
    def draw(self,screen):
        if self.visible:
            screen.blit(self.image, self.rect)
# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()