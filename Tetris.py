from Tetromino import Tetromino
from helper import *

# TODO: Add functions for controls, handling line clears, etc.
class Tetris:
	def __init__(self, parent):
		self.parent = parent
		self.surface = pygame.Surface((BOARD_SURFACE_WIDTH, BOARD_SURFACE_HEIGHT))
		self.displaySurface = pygame.display.get_surface()
		self.allTetrominoes: list[Tetromino] = []

	def drawGrid(self):
		for gridC in range(1, BOARD_WIDTH):
			scC = gridC * TILE_SIZE
			pygame.draw.line(self.surface, colours["white"], (scC, 0), (scC, BOARD_SURFACE_HEIGHT))

		for gridR in range(1, BOARD_HEIGHT):
			scR = gridR * TILE_SIZE
			pygame.draw.line(self.surface, colours["white"], (0, scR), (BOARD_SURFACE_WIDTH, scR))
			
	def drawTetrominoes(self):
		pass
		# for tetromino in self.allTetrominoes:
		# 	tetromino.draw()

	def addTetromino(self, tetrominoType=None, colour=None, current=False):
		self.allTetrominoes.append(Tetromino(self, tetrominoType, colour, current))

	def controls(self):
		pass

	def update(self):
		pass
		# for tetromino in self.allTetrominoes:
		# 	tetromino.update()

	def draw(self):
		self.surface.fill(colours["black"])
		self.drawGrid()
		self.drawTetrominoes()
		self.displaySurface.blit(self.surface, (BOARD_OFFSETX, BOARD_OFFSETY))