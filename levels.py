import random, constants
from player import Player
from asteroid import Asteroid
from bullet import Bullet

class level:
	player = None
	asteroid_list = []
	bullet_list = []
	
class level1(level):
	def __init__(self, player):
		'''
		self.asteroid_list = [Asteroid(0, 0, random.choice[2, -2], random.choice[2, -2], self), Asteroid(0, constants.SCREEN_HEIGHT - 43, random.choice[2, -2], random.choice[2, -2], self),
		Asteroid(250, 100, 2, -2, self)]
		'''
		self.player = player
		for i in range(0, 5):
			self.asteroid_list.append(Asteroid(random.randint(0, constants.SCREEN_WIDTH - 43), random.randint(0, constants.SCREEN_HEIGHT - 43), 
			random.choice([2, -2]), random.choice([2, -2]), self))