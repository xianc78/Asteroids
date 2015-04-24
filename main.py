import pygame, sys, random
import constants
import levels
import text
from asteroid import Asteroid
from player import Player
pygame.init()

def update_screen():
	global lifeCounter
	screen.fill(constants.BLACK)
	for bullet in current_level.bullet_list:
		screen.blit(bullet.image, (bullet.rect.x, bullet.rect.y))
	screen.blit(player.image, (player.rect.x, player.rect.y))
	for asteroid in current_level.asteroid_list:
		screen.blit(asteroid.image, (asteroid.rect.x, asteroid.rect.y))
	screen.blit(lifeCounter.text, lifeCounter.rect)
		
def titleScreen():
	global screen
	titleText = text.titleText()
	screen.fill(constants.BLACK)
	screen.blit(titleText.text, titleText.rect)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				return None
		pygame.display.update()
		
def pause():
	global screen
	pauseText = text.pauseText()
	screen.blit(pauseText.text, pauseText.rect)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				return None
		pygame.display.update()
		
def levelClear():
	levelText = text.levelComplete()
	screen.blit(levelText.text, levelText.rect)
	pygame.display.update()
	pygame.time.wait(500)

def main():
	global screen, current_level, player, lifeCounter
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	lifeCounter = text.lifeCounter()
	
	titleScreen()
	
	player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
	level_list = [levels.level1, levels.level2]
	levelno = 1
	current_level = level_list[levelno - 1](player)
	player.level = current_level
	
	while True:
		pygame.display.set_caption("Asteroids")
		lifeCounter.text = lifeCounter.font.render("Life: " + str(player.lives), True, constants.WHITE)
		update_screen()
		'''
		screen.fill(constants.BLACK)
		for bullet in current_level.bullet_list:
			screen.blit(bullet.image, (bullet.rect.x, bullet.rect.y))
		screen.blit(player.image, (player.rect.x, player.rect.y))
		for asteroid in current_level.asteroid_list:
			screen.blit(asteroid.image, (asteroid.rect.x, asteroid.rect.y))
		'''
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					player.shoot()
				elif event.key == pygame.K_LCTRL:
					player.jump()
				elif event.key == pygame.K_ESCAPE:
					pause()
		player.change_x = 0
		player.change_y = 0
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_UP]:
			player.change_y = -5
			player.facing = "up"
		elif pressed[pygame.K_DOWN]:
			player.change_y = 5
			player.facing = "down"
		elif pressed[pygame.K_LEFT]:
			player.change_x = -5
			player.facing = "left"
		elif pressed[pygame.K_RIGHT]:
			player.change_x = 5
			player.facing = "right"
			'''
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					player.change_y += -5
				elif event.key == pygame.K_DOWN:
					player.change_y += 5
				elif event.key == pygame.K_LEFT:
					player.change_x += -5
				elif event.key == pygame.K_RIGHT:
					player.change_x += 5
				
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					player.change_y += 5
				elif event.key == pygame.K_DOWN:
					player.change_y += -5
				elif event.key == pygame.K_LEFT:
					player.change_x += 5
				elif event.key == pygame.K_RIGHT:
					player.change_x += -5
			'''
		player.update()
		for asteroid in current_level.asteroid_list:
			asteroid.update()
		for bullet in current_level.bullet_list:
			bullet.update()
		if len(current_level.asteroid_list) == 0:
			update_screen()
			pygame.display.update()
			levelClear()
			levelno += 1
			if levelno > len(level_list):
				pygame.quit()
				sys.exit()
			else:
				current_level = level_list[levelno - 1](player)
				player.level = current_level
		pygame.display.update()
		clock.tick(constants.FPS)
		
if __name__ == "__main__":
	main()