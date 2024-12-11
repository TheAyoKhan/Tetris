from helper import *

class ScoreScreen:
	def __init__(self, parent):
		self.parent = parent
		self.surface = pygame.Surface()
		self.score = 0

	def draw(self):
		pass

class NextTetrominoes:
	def __init__(self, parent, nextTetrominoes = []):
		self.parent = parent
		self.surface = pygame.Surface()
		self.nextTetrominoes = nextTetrominoes

	def draw(self):
		pass

class InfoBox:
	def __init__(self, parent, nextTetrominoes = []):
		self.parent = parent
		self.surface = pygame.Surface()
		self.displaySurface = pygame.display.get_surface()
		self.scoreScreen = ScoreScreen(self)
		self.nextPieces = NextTetrominoes(self, nextTetrominoes)

	def draw(self):
		self.scoreScreen.draw()
		self.nextPieces.draw()
		self.displaySurface.blit(self.surface, )