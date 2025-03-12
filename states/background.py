from settings import *
from support import *


class BG(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)

        self.image = import_image(BACKGROUNDS['stage 3'])
        self.image = pygame.transform.scale_by(self.image, 0.8)
        self.rect = self.image.get_frect(topleft = (0,0))

        self.direction = -1
        self.speed = 50

    def move(self, dt):
        self.rect.x += self.direction * self.speed * dt
        if self.rect.right <= WINDOW_WIDTH:
            self.rect.left = 0

    def update(self, dt):
        self.move(dt)