#import pygame
import pygame
#import constants from contants file.
from constants import *


def main():
	#check if pygame is initalized, if not initalize it
	if pygame.get_init() != True:
		pygame.init()
	#lock FPS to 60
	fps_limit = pygame.time.Clock()
	dt = 0 #delta time

	#print width and height
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	#set screen surface variables
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	screen_color = (0,0,0) #set screen color using RGB
	#infinite loop to run game
	game_run = 1
	while game_run == 1:
		#for loop to close game when "x" is pressed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		#draw screen
		screen.fill(screen_color)
		pygame.display.flip()
		#use fps_limit to keep refresh at 60 fps
		fps_limit.tick(60)
		dt = (fps_limit.get_time()/1000) #calculate delta time

if __name__ == "__main__":
	main()

