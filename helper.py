import pygame

# Helper tools for pygame
# Might use this if calculating everything gets too hard
vec2 = pygame.math.Vector2

# Needed variables throughout code, can be adjused as seen fit
TILE_SIZE = 30
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 800
BOARD_WIDTH, BOARD_HEIGHT = 10, 20
BOARD_SURFACE_WIDTH, BOARD_SURFACE_HEIGHT = TILE_SIZE*BOARD_WIDTH, TILE_SIZE*BOARD_HEIGHT
BOARD_OFFSETX, BOARD_OFFSETY = 2*TILE_SIZE, 3*TILE_SIZE
INFOBOX_WIDTH, INFOBOX_HEIGHT = 8, 20
INFOBOX_SURFACE_WIDTH, INFOBOX_SURFACE_HEIGHT = TILE_SIZE*INFOBOX_WIDTH, TILE_SIZE*INFOBOX_HEIGHT


colours = {
	"black": (0, 0, 0),
	"grey": (100, 100, 100),
	"white": (255, 255, 255),
	"red": (255, 0, 0),
	"green": (255, 0, 0),
	"lblue": (0, 255, 255),
	"blue": (0, 0, 255),
	"purple": (255, 0, 255),
	"orange": (255, 150, 0),
	"yellow": (255, 255, 0),
}

# TODO: Need to decide how to best represent each tetrimino
# TODO: Finish the tetriminoes
# Ideas: one relative position type, rotated using matrices/manually
# OR hardcode each rotation value. Much easier, but not as impressive nor as easily modifiable
TETRIMINO_TYPES = {
	"I": {
		"colour": colours["lblue"],
		"relPos": [(0, 0), (1, 0), (-1, 0), (-2, 0)],
	},
	"O": {
		"colour": colours["yellow"],
		"relPos": [(0, 0), (0, -1), (1, 0), (1, -1)]
	},
	"T": {
		"colour": colours["purple"],
		"relPos": [(0, 0), (1, 0), (-1, 0), (0, 1)],
	},
	"J": {
		"colour": colours["blue"],
		"relPos": [(0, 0), (-1, 0), (-1, -1), (0, -1)],
	},
	"L": {
		"colour": colours["orange"],
		"relPos": [(0, 0), (-1, 0), (-1, -1), (0, -1)],
	},
	"S": {
		"colour": colours["green"],
		"relPos": [(0, 0), (-1, 0), (-1, -1), (0, -1)]
	},
	"Z": {
		"colour": colours["red"],
		"relPos": [(0, 0), (-1, 0), (-1, -1), (0, -1)]
	}
}