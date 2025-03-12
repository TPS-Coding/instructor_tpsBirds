import asyncio
import pygame, sys
import settings as config
from random import choice

from states.menu import Menu
from states.gameplay import GamePlay
from states.game_over import GameOver
from game import Game


pygame.init()
display_surface = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
pygame.display.set_caption("TPS BIRDS")

states = {
    "MENU": Menu(),
    "GAMEPLAY": GamePlay(),
    "GAMEOVER": GameOver()
}


game = Game(display_surface, states, "MENU")
asyncio.run(game.run())
