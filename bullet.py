import pygame
import constants
pygame.init()

class Bullet:
	def __init__(self, x, y, change_x, change_y, level):
		self.image = pygame.Surface([5, 5])
		self.image.fill(constants.WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.change_x = change_x
		self.change_y = change_y
		self.level = level
		
	def update(self):
		self.rect.x += self.change_x
		if (self.rect.bottom < 0) or (self.rect.top > constants.SCREEN_HEIGHT):
			self.level.bullet_list.remove(self)
		self.rect.y += self.change_y
		if (self.rect.left < 0) or (self.rect.right > constants.SCREEN_WIDTH):
			self.level.bullet_list.remove(self)