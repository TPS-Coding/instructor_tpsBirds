import asyncio
import pygame
import sys
from settings import *


class Game(object):
    def __init__(self, window, states, start_state):
        self.done = False
        self.window = window
        self.clock = pygame.time.Clock()
        self.fps = 120
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]
        

    def event_loop(self):
        for event in pygame.event.get():
            self.state.get_event(event)

    def flip_state(self):
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)

    def update(self, dt):
        if self.state.quit:
            self.done = True

        elif self.state.done:
            self.flip_state()

        self.state.update(dt)

    def draw(self):
        self.state.draw(self.window)

    async def run(self):
        while not self.done:
            dt = 0.16
            self.event_loop()
            self.update(dt)
            self.draw()
            pygame.display.update()
            self.clock.tick(60)
            await asyncio.sleep(0)
        # Closing the game
        pygame.quit()
        sys.exit()