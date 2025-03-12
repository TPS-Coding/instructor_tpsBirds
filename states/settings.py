import pygame
import sys, time
from random import randint, choice

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
SCREEN_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
FRAMERATE = 120
ANIMATION_SPEED = 1

pygame.mixer.init()


BACKGROUNDS = {
    'stage 1':"graphics/backgrounds/1",
    'stage 2':"graphics/backgrounds/2",
    'stage 3': "graphics/backgrounds/Repeated"
}
EFFECTS = {
    'poof': 'graphics/deadsprite',
    'fire': 'graphics/effects/flame1',
    'fireball': 'graphics/effects/flame10',
    'fire_poof': 'graphics/effects/flame2'
}

BIRDS = {
    'bird1': "graphics/birds/Bird01",
    'bird4': "graphics/birds//Bird04",
    'bird7': "graphics/birds//Bird07"
}

OBSTACLES = {
    'ob1' : "graphics/backgrounds/Obstacle1",
    'ob2' : "graphics/backgrounds/Obstacle2"
}

"""
SOUNDS = {
			'jump': pygame.mixer.Sound("audio/jump.ogg"),
            'fire': pygame.mixer.Sound("audio/fireloop.ogg")
		}
"""