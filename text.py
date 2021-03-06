import pygame
import constants
pygame.init()

class textObj:
	font = pygame.font.SysFont("arial", 32)
	text = None
	
class titleText(textObj):
	def __init__(self):
		self.text = self.font.render("Some Asteroids Clone", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

class pauseText(textObj):
	def __init__(self):
		self.text = self.font.render("Paused", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
		
class lifeCounter(textObj):
	def __init__(self):
		self.text = self.font.render("Life: ", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.x = 0
		self.rect.y = 0

class scoreCounter(textObj):
	def __init__(self):
		self.text = self.font.render("Score: ", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.bottomleft = (0, constants.SCREEN_HEIGHT)
		
# Work on these later.		
		
class levelComplete(textObj):
	def __init__(self):
		self.text = self.font.render("Level Clear", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
		
class gameOver(textObj):
	def __init__(self):
		self.text = self.font.render("Game Over", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)