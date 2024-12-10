from helper import pygame
from Tetris import Tetris

class Game:
	def __init__(self, width, height):
		self.screen_width = width
		self.screen_height = height

	def initialize_game(self):
		pygame.init()
		screen = pygame.display.set_mode((self.screen_width, self.screen_height))

		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					print("Quitting")
					running = False
			
			# Set default background colour
			screen.fill((0, 0, 0))
			
			pygame.display.update()

	def start_match(self):
		pass
