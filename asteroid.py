import pygame, sys, random
import constants
pygame.init()

explosionSound = pygame.mixer.Sound("resources/explosion.wav")

class Asteroid:
	def __init__(self, x, y, change_x, change_y, level):
		try:
			self.image = pygame.image.load("resources/asteroid.png")
		except pygame.error:
			print "asteroid.png has been deleted."
			raw_input("<press enter to continue>")
			pygame.quit()
			sys.exit()
		self.level = level
		self.player = self.level.player
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		while True:
			if self.rect.colliderect(self.level.player.rect):
				self.rect.x = random.randint(0, constants.SCREEN_WIDTH - self.rect.width)
				self.rect.y = random.randint(0, constants.SCREEN_HEIGHT - self.rect.height)
			else:
				break
		self.change_x = change_x
		self.change_y = change_y
	
	def update(self):
		self.rect.x += self.change_x
		if (self.rect.left <= 0) or (self.rect.right >= constants.SCREEN_WIDTH):
			self.change_x *= -1
		self.rect.y += self.change_y
		if (self.rect.top <= 0) or (self.rect.bottom >= constants.SCREEN_HEIGHT):
			self.change_y *= -1
		for bullet in self.level.bullet_list:
			if self.rect.colliderect(bullet.rect):
				self.level.bullet_list.remove(bullet)
				self.level.asteroid_list.remove(self)
				explosionSound.play()
				
# Work in progress

class AsteroidSmall:
	def __init__(self):
		pass