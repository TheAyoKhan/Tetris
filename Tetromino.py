import random
from helper import *

class Mino:
	def __init__(self, parent: 'Tetromino', position):
		self.parent = parent
		self.rect = pygame.Rect()
		self.containerRect = self.parent.rect
		self.colour = parent.getColour()
		self.position = position

		def draw(self):
			pass

		# TODO: Create out of bounds check
		# TODO: Collision with other players check?
		def checkCollision(self):
			pass
			
		# TODO: Probably remake the rotation formula with relative coordinates based on self.position
		def rotate(self, clockwise = True):
			# Because the coordinate system is left-handed, the matrices are a little different than normal
			"""
			CW matrix = [0 -1]
									[1  0]
			Matrix multiplication with x and y coord turns into:
				(x, y) --> (-y, x)

			CCW matrix = [0  1]
									 [-1 0]
			Matrix multiplication with x and y coord turns into:
				(x, y) --> (y, -x)
			"""
			x, y = self.position
			newPos = (-y, x) if clockwise else (y, -x)
			return newPos
		
		def update():
			pass

class Tetromino:
	# https://en.wikipedia.org/wiki/Tetromino#One-sided_tetrominoes for reference

	def __init__(self, parent, tetrominoType=None, colour=None, current=False):
		self.parent = parent
		self.rect = pygame.Rect()
		self.type = tetrominoType if tetrominoType in self.tetrominoes.keys() else random.choice(self.tetrominoes.keys())
		self.current = current

		self.rotation = 0
		# self.minoes[0] will be the pivot/origin
		self.minoes = [Mino(coord) for coord in TETRIMINO_TYPES[self.type]["relPos"]]
		self.colour = colour if colour in colours.keys() else TETRIMINO_TYPES[self.type]["color"]

	def update(self):
		for mino in self.minoes:
			mino.updateMino()
	
	# TODO: program some way to account for shifts for pieces that kick off walls or rotate strangely
	def rotate(self, clockwise = True):
		# deg = 1: 90; deg = 2: 180; deg = 3; 270
		tempRotation = self.rotation
		tempRotation += 1 if clockwise else -1
		self.rotation = tempRotation % 4

		for mino in self.minoes:
			mino.rotate(clockwise)
	
	# Will need to use this for rotations, so that rotations of the O/I/L/J blocks, don't mess up
	def getOffset(self):
		# https://tetris.wiki/Super_Rotation_System#Wall_Kicks will help with wall kick section
		pass

	def draw(self):
		for mino in self.minoes:
			mino.draw()
	
	def getShape(self) -> list[tuple[int, int]]:
		return TETRIMINO_TYPES[self.type].relPos
	
	def getColour(self):
		return self.colour

	# Idea: Return something in the form of (bool: whether there is a collision, obj: reference to the other object)
	# The idea of only boolean works, but might not with other players.
	def checkCollision(self):
		for mino in self.minoes:
			if mino.checkCollision():
				return True
		return False
	