import sys
#import pygame
import pygame
#import constants from contants file.
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shoot


def main():
	#check if pygame is initalized, if not initalize it
	if pygame.get_init() != True:
		pygame.init()
	#lock FPS to 60
	fps_limit = pygame.time.Clock()
	dt = 0 #delta time

	#create groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shoot.containers = (shots, updatable, drawable)
	#create asteroid field to spawn asteroids
	asteroidfield = AsteroidField()

	#print starting message
	print("Starting asteroids!")
	#set screen surface variables
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	screen_color = (0,0,0) #set screen color using RGB
	#create player token in middle of screen
	player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
	
	#infinite loop to run game
	game_run = 1
	while game_run == 1:
		#use fps_limit to keep refresh at 60 fps
		fps_limit.tick(60)
		#for loop to close game when "x" is pressed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		#draw background screen
		screen.fill(screen_color)

		#update player movement before drawing
		updatable.update(dt)

		if player.timer > 0:
			player.timer -= dt

		#check for collision with player
		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game Over")
				sys.exit()
		
			#check for collision with bullet
			for shot in shots:
				if asteroid.collision(shot):
					shot.kill()
					asteroid.split()

		#draw player token each frame
		for obj in drawable:
			obj.draw(screen)

		#refresh frame - always have at the end
		pygame.display.flip()

		dt = (fps_limit.tick(60)/1000) #calculate delta time
		

		

if __name__ == "__main__":
	main()

