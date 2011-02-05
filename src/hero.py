#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
from funciones import *

# Clases
# ---------------------------------------------------------------------

class Hero(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image("Graphics/Hero/D1.png",True)
		self.rect = self.image.get_rect()
		self.anima = 0
		self.rect.centerx = WIDTH / 2
		self.rect.centery = HEIGHT / 2
		self.speed = [0.2, -0.2]
#------------------------------------------------------------------------------ 
	def anim(self, n1, n2, n3):
		self.anima = self.anima + 1
		if self.anima == 7:
			self.image = load_image(n2, True)
		if self.anima == 15:
			self.image = load_image(n1, True)
		if self.anima == 22:
			self.image = load_image(n3, True)
		if self.anima == 30:
			self.image = load_image(n1, True)
			self.anima = 0
#------------------------------------------------------------------------------ 
	def move(self, time, keys):
		if self.rect.top >= 0:
			if keys[K_UP]:
				self.rect.centery -= self.speed[0] * time
				self.anim("Graphics/Hero/U1.png","Graphics/Hero/U2.png","Graphics/Hero/U3.png")

		if self.rect.bottom <= HEIGHT:
			if keys[K_DOWN]:
				self.rect.centery += self.speed[0] * time
				self.anim("Graphics/Hero/D1.png","Graphics/Hero/D2.png","Graphics/Hero/D3.png")

		if self.rect.left >= 0:
			if keys[K_LEFT]:
				self.rect.centerx += self.speed[1] * time
				self.anim("Graphics/Hero/L1.png","Graphics/Hero/L2.png","Graphics/Hero/L3.png")
		
		if self.rect.right <= WIDTH:
			if keys[K_RIGHT]:
				self.rect.centerx -= self.speed[1] * time
				self.anim("Graphics/Hero/R1.png","Graphics/Hero/R2.png","Graphics/Hero/R3.png")
# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

def main():	
	return 0

if __name__ == '__main__':
	main()
