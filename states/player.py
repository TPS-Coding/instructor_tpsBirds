from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, surfs):
        super().__init__(groups)

        self.frames = surfs
        self.frame_index = 0
        self.animation_speed = 5

        self.image = self.frames[self.frame_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH*0.2, WINDOW_HEIGHT/2))

        self.velocity = 0
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.gravity = 10

    def apply_gravity(self,dt):
        self.velocity += self.gravity * dt
        self.pos.y += self.velocity * dt
        self.rect.y = round(self.pos.y)

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.velocity = -50
            #SOUNDS['jump'].play()

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        self.image = pygame.transform.scale_by(self.frames[int(self.frame_index % len(self.frames))], 1)


    def update(self,dt):
        self.apply_gravity(dt)
        self.jump()
        self.animate(dt)