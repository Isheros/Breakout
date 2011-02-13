#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import cPickle
# Pygame
from pygame.locals import *
# Engine
from Core.funciones import *
from Core.scene import *
from config import *
# Juego
from ball import *
from pad import *

from mgr_brick import *
from mgr_vidas import *
from mgr_puntos import *
from mgr_puntuaciones import *

from scene_gameover import *

# Clases
# ---------------------------------------------------------------------
class SceneGame(Scene):
    """Escena del juego, esta es la escena donde se
    desarrolla todo el juego."""
    def __init__(self, director):
        Scene.__init__(self, director)
        # Inicia Pelota.
        self.ball = Ball()
        # Inicia Pad.
        self.pad = Pad()
        # Inicia Ladrillos.
        self.brick_mgr = BrickMgr()
        # Inicia Vidas.
        self.vidas = Vidas()
        self.vidas.setVidas(3)
        # Inicia Puntos.
        self.puntos = Puntos()
    
    def on_update(self):
        self.time = self.director.time
        # Actualiza Pala.
        self.pad.update(self.time)
        # Actualiza Bola.
        self.ball.update(self.time)
        # Actualiza Ladrillos.
        self.brick_mgr.update(self.ball)
        
        # Resta Vidas al escaparse la Bola.
        if self.ball.resVida:
            self.vidas.resVidas()
            self.ball.resVida = False
            
        # Agrega Puntos al romper Ladrillos.
        if self.ball.addPuntos:
            self.puntos.addPuntos(100)
            self.ball.addPuntos = False
            
        # Si se terminan las vidas llama a GameOver.
        if self.vidas.getVidas() <= 0:
            self.highscores = Puntuaciones(self.puntos.getPuntos())
            self.highscores.replace()
            self.director.change_scene(SceneOver(self.director))
        
        # Si la bola es pegajosa.
        if self.ball.getSticky():
            # La mueve junto con la pala.
            self.ball.setPos(self.pad.getPosX()
                             ,self.pad.getPosY()-self.pad.getHeight())
        
        # Si colisiona la bola con el pad.
        if checkCollision(self.ball,self.pad):
            # Llama los metodos onCollide.
            self.ball.onCollide(self.pad)
            self.pad.onCollide(self.ball)
            
    
    def on_event(self):
        # Mueve pala a la izquierda.
        if self.director.key[pygame.K_LEFT]:
            self.pad.setDir(1, self.time)
        # Mueve pala a la derecha.
        if self.director.key[pygame.K_RIGHT]:
            self.pad.setDir(2, self.time)
        # Despega pelota.
        if self.director.key[pygame.K_SPACE] and self.ball.getSticky():
            self.ball.setSticky(False) 
        
    def on_draw(self,screen):
        # Limpia pantalla.
        screen.fill(0x999999)
        # Dibuja en pantalla la Pelota.
        self.ball.draw(screen)
        # Dibuja en pantalla la Pala.
        self.pad.draw(screen)
        # Dibuja en pantalla los Ladrillos.
        self.brick_mgr.draw(screen)
        # Dibuja en pantalla las Vidas.
        self.vidas.draw(screen)
        # Dibuja en pantalla los Puntos.
        self.puntos.draw(screen)
# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()