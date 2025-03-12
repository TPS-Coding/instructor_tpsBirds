import pygame
import settings as config
from .support import import_image

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, orientation):
            super().__init__(groups)

                
            self.image = import_image(config.OBSTACLES[orientation]) 
            self.height = self.image.get_height()
            self.width = self.image.get_width()

            self.image = pygame.transform.scale(self.image, (self.width, self.height*2))
            self.mask = pygame.mask.from_surface(self.image)
            self.speed = 50
                

            self.rect = self.image.get_frect(midtop = (x,y))

            self.pos = pygame.math.Vector2(self.rect.topleft)


    def move(self, dt):
            self.pos.x -= self.speed * dt
            self.rect.x = round(self.pos.x)
            if self.rect.right <= -400:
                self.kill()

    def update(self, dt):
        self.move(dt)


