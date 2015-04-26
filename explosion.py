import pygame
import constants
pygame.init()

explosionSound = pygame.mixer.Sound("resources/explosion.wav")

class Explosion:
	def __init__(self, x, y, level):
		self.image = pygame.image.load("resources/explosion.png")
		self.image.set_colorkey(constants.WHITE)
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.life = 20
		self.level = level
		explosionSound.play()
		
	def update(self):
		self.life -= 1
		if self.life <= 0:
			self.level.explosion_list.remove(self)