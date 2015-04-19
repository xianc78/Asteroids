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