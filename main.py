#import pygame
import pygame
#import constants from contants file.
from constants import *


def main():
	#check if pygame is initalized, if not initalize it
	if pygame.get_init() != True:
		pygame.init()
	#print width and height
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	#draw screen surface
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	screen_color = (0,0,0)
	game_run = 1
	while game_run == 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(screen_color)
		pygame.display.flip()

if __name__ == "__main__":
	main()

