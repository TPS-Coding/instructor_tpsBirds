import pygame
from settings import *
from random import randint

class Death(pygame.sprite.Sprite):
    def __init__(self, groups,frames,player_pos):
        super().__init__(groups)

        self.frames = frames
        self.frame_index = 0
        self.offset = pygame.math.Vector2(50,-50)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(midtop = player_pos + self.offset)


        self.animation_speed = 5

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.index = int(self.frame_index % len(self.frames))
        self.image = self.frames[self.index]


    def update(self, dt):
        self.animate(dt)


        
class Fire(pygame.sprite.Sprite):
    def __init__(self, groups,frames,player_pos):
        super().__init__(groups)

        self.frames = frames
        self.frame_index = 0
        self.offset = pygame.math.Vector2(50,-50)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(midtop = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

        self.animation_speed = 3

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        if self.frame_index > len(self.frames):
            self.kill()
        else:
            self.index = int(self.frame_index % len(self.frames))
        self.image = self.frames[self.index]


    def update(self, dt):
        self.animate(dt)

class FireBall(pygame.sprite.Sprite):
    def __init__(self, groups, surfs):
        super().__init__(groups)

        self.frames = surfs
        self.frame_index = 0

        y_pos = randint(10, WINDOW_HEIGHT - 10)
        x_pos = WINDOW_WIDTH + 50

        self.image = self.frames[self.frame_index]
        self.image = pygame.transform.rotate(self.image, 180)
        self.image = pygame.transform.scale_by(self.image, 0.3)
        self.rect = self.image.get_frect(midleft =(x_pos, y_pos))

        self.animation_speed = 1
        self.direction = -1
        self.speed = 100

    def move(self, dt):
        self.rect.x += self.direction * self.speed * dt

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        if self.frame_index > len(self.frames):
            self.kill()
        else:
            self.index = int(self.frame_index % len(self.frames))
        self.image = pygame.transform.rotate(self.frames[self.index], 180)
        self.image = pygame.transform.scale_by(self.image, 0.3)


    def update(self, dt):
        self.move(dt)
        self.animate(dt)

class FirePoof(pygame.sprite.Sprite):
    def __init__(self, groups,frames,player_pos):
        super().__init__(groups)

        self.frames = frames
        self.frame_index = 0
        self.offset = pygame.math.Vector2(50,-50)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center = player_pos)


        self.animation_speed = 1

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        if self.frame_index > len(self.frames):
            self.kill()
        else:
            self.index = int(self.frame_index % len(self.frames))
        self.image = self.frames[self.index]


    def update(self, dt):
        self.animate(dt)


