import pygame, random, sys, math
import constants
from bullet import Bullet
pygame.init()

class Player:
	def __init__(self, x, y):
		self.facing = "up"
		try:
			image = pygame.image.load("resources/ship.png")
			image = pygame.transform.scale(image, (40, 40))
		except pygame.error:
			print "ship.png has been deleted."
			raw_input("<press enter to continue>")
			pygame.quit()
			sys.exit()
		self.images = []
		self.images.append(image)
		self.images.append(pygame.transform.rotate(image, 90))
		self.images.append(pygame.transform.rotate(image, 180))
		self.images.append(pygame.transform.rotate(image, 270))
		self.image = self.images[0]
		self.rect = self.image.get_rect()
		'''
		self.speed = 0.0
		self.rotspeed = 0
		self.direction = 270
		'''
		self.rect.x = x
		self.rect.y = y
		self.change_x = 0
		self.change_y = 0
		
	def update(self):
		if self.facing == "down":
			self.image = self.images[2]
		elif self.facing == "up":
			self.image = self.images[0]
		elif self.facing == "right":
			self.image = self.images[3]
		elif self.facing == "left":
			self.image = self.images[1]
		self.rect.x += self.change_x
		if self.rect.x < 0:
			self.rect.x = 0
		elif self.rect.right > constants.SCREEN_WIDTH:
			self.rect.right = constants.SCREEN_WIDTH
		self.rect.y += self.change_y
		if self.rect.y < 0:
			self.rect.y = 0
		elif self.rect.bottom > constants.SCREEN_HEIGHT:
			self.rect.bottom = constants.SCREEN_HEIGHT
		for asteroid in self.level.asteroid_list:
			if self.rect.colliderect(asteroid.rect):
				pygame.quit()
				sys.exit()
		
	def change_speed(self, x, y):
		self.change_x += x
		self.change_y += y
		
	def shoot(self):
		if self.facing == "up":
			change_x = 0
			change_y = -8
		elif self.facing == "down":
			change_x = 0
			change_y = 8
		elif self.facing == "left":
			change_x = -8
			change_y = 0
		elif self.facing == "right":
			change_x = 8
			change_y = 0
		self.level.bullet_list.append(Bullet(self.rect.centerx, self.rect.centery, change_x, change_y, self.level))
	
	def jump(self):
		while True:
			self.rect.x = random.randint(0, constants.SCREEN_WIDTH - self.rect.width)
			self.rect.y = random.randint(0, constants.SCREEN_HEIGHT - self.rect.height)
			for asteroid in self.level.asteroid_list:
				if self.rect.colliderect(asteroid.rect):
					continue
				else:
					break