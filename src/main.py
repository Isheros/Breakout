#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
from pygame.locals import *
# Engine
from Core.funciones import *
from Core.director import *
# Juego
from scene_intro import SceneIntro

def main():
    # Inicializa director y primera escena.
    dir = Director()
    # Pasa a la primera escena y empieza el bucle.
    dir.change_scene(SceneIntro(dir))
    dir.loop()

if __name__ == '__main__':
    pygame.init()
    main()