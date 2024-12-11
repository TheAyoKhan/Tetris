from helper import *
from Tetris import Tetris

class Game:
	def __init__(self, width, height):
		self.screen_width = width
		self.screen_height = height
		self.board = None
		self.matchStarted = False
		self.deltaTime = 0

	def initializeGame(self):
		pygame.init()
		screen = pygame.display.set_mode((self.screen_width, self.screen_height))
		running = True

		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					print("Quitting")
					running = False
					break
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.startMatch()
			# Set default background colour
			screen.fill(colours["grey"])

			if self.matchStarted:
				self.playMatch()
			
			pygame.display.update()

	# To use only for physics calculations, i.e. dropping blocks
	def fixedUpdate(self):
		pass

	def startMatch(self):
		self.matchStarted = True
		self.board = Tetris(self)

	def playMatch(self):
		self.board.draw()
