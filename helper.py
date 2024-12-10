import pygame

# Helper tools for pygame
vec2 = pygame.math.Vector2

# Needed variables throughout code
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

colours = {
	"red": (255, 0, 0),
	"green": (255, 0, 0),
	"lightblue": (0, 255, 255),
	"blue": (0, 0, 255),
	"purple": (255, 0, 255),
	"orange": (255, 150, 0),
	"yellow": (255, 255, 0),
}

# TODO: Need to decide how to best represent each tetrimino
# TODO: Finish the tetriminoes
# Ideas: one relative position type, rotated using matrices/manually
# OR hardcode each rotation value. Much easier, but not as impressive nor as easily modifiable
tetriminoes = {
	"I": {
			"colour": colours.lightblue,
			"relpos": [(0, 0), (1, 0), (-1, 0), (-2, 0)],
	},
	"O": {
		"colour": colours.yellow,
		"relPos": [(0, 0), (0, -1), (1, 0), (1, -1)]
	},
	"T": {
		"colour": colours.purple,
		"relPos": [(0, 0), (1, 0), (-1, 0), (0, 1)],
	},
	"J": {
		"colour": colours.blue,
		"relPos": [(0, 0), (-1, 0), (-1, -1), (0, -1)],
	},
	"L": {
		"colour": colours.orange,
		"relPos": [(0, 0), (-1, 0), (-1, -1), (0, -1)],
	},
	"S": {
		"colour": colours.green,
		"relPos": [(0, 0), (-1, 0), (-1, -1), (0, -1)]
	},
	"Z": {
		"colour": colours.red,
		"relPos": [(0, 0), (-1, 0), (-1, -1), (0, -1)]
	}
}