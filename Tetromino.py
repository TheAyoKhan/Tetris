import random
from helper import tetriminoes, vec2

class Mino:
	def __init__(self, parent):
		self.parent = parent
		self.colour = parent.getColour()

		def drawMino(self):
			pass

		def checkCollision(self):
			pass
			# Out of bounds check
			
			# TODO: eventual collision with other players check?
			
		def rotateTile(self, clockwise = True):
			# TODO: either use rotation matrices or manually rotate the points using
			pass


class Tetromino:
	# TODO: Find a way to represent a teris piece
	# https://en.wikipedia.org/wiki/Tetromino#One-sided_tetrominoes for referenc

	def __init__(self, parent, type = None, colour = None):
		self.parent = parent
		self.type = type if type in self.tetrominoes.keys() else random.choice(self.tetrominoes.keys())
		self.rotation = 0
		self.minoes = [Mino(coord) for coord in tetriminoes[self.type][self.rotation]]
		self.colour = tetriminoes[self.type] if colour else tetriminoes[self.type].colour

	def getPosition(self):
		return self.position
	
	def rotate(self, deg = 1):
		# TODO: find some way to check the number of possible rotations, i.e. 4 for L/J/T, 2 for I/S/Z, 1 for O
		# deg = 1: 90; deg = 2: 180; deg = 3; 270
		# self.rotation = (self.rotation + deg) % ???
		pass
	
	def getShape(self):
		return 

	def drawTetrimino(self):
		pass
	
	def getShape(self) -> list[tuple[int, int]]:
		return self.tetrominoes[self.type][self.rotation]
	
	def getColour(self):
		return self.colour

	# TODO: Should return something in the form of (bool: whether there is a collision, obj: reference to the other object)
	def checkCollision(self):
		collision = False
		for mino in self.minoes:
			collision = collision or mino.checkCollision()
	