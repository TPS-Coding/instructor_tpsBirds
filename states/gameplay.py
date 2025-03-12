import pygame

from .player import Player
from .obs import Obstacle
from .background import BG
from .base import BaseState
import settings as config
from .background import BG
from .timer import Timer
from support import *
from .death import *

class GamePlay(BaseState):
    def __init__(self):
        super(GamePlay, self).__init__()
        self.next_state = "GAMEOVER"
        self.status = ""
        self.score = 0
        self.time_active = 0
        self.paused = False

        self.load_assets()

        self.timers = {
            'score': Timer(1500, autostart=True),
            'obstacle': Timer(1500, autostart=True),
            'hit':Timer(2000, autostart=True),
            'fireball': Timer(3000),
        }
        #Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.fire_sprites = pygame.sprite.Group()

        ##Sprites
        self.bg = BG(self.all_sprites)
        self.player = Player(self.all_sprites, self.player_frames)

        ## Text
        self.score_text = self.font.render(f'Score : {self.score}',True, pygame.Color("white"))
        self.score_rect = self.score_text.get_frect(topleft = (WINDOW_WIDTH/2, 10))

        self.paused_text = self.med_font.render("PAUSED", True, pygame.Color("red"))
        self.paused_rect = self.paused_text.get_frect(center = (config.WINDOW_WIDTH/2, config.WINDOW_HEIGHT/2))

    def get_event(self,event):
        if event.type == pygame.QUIT:
            self.quit = True
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                if not self.paused:
                    self.paused = True
                else:
                    self.paused = False

    def load_assets(self):
        self.player_frames = import_folder(config.BIRDS['bird1'])
        self.font = pygame.font.Font("graphics/font/BD_Cartoon_Shout.ttf", 30)
        self.poof_surfs = import_folder(config.EFFECTS['poof'])
        self.fire_surfs = import_folder(config.EFFECTS['fire'])
        self.med_font = pygame.font.Font("graphics/font/BD_Cartoon_Shout.ttf", 30)
        self.fireball_surfs = import_folder(config.EFFECTS['fireball'])
        self.firepoof_surfs = import_folder(config.EFFECTS['fire_poof'])

    def startup(self, persistent):
        self.persist["score"] = 0
        self.score = 0
        self.time_active = 0
        self.all_sprites.empty()
        self.collision_sprites.empty()
        self.all_sprites.add(self.bg)
        self.player = Player(self.all_sprites, self.player_frames)
        

    def add_score(self):
        if not self.timers['score'].active:
            self.score += 20
            self.timers['score'].activate()
            self.score_text = self.font.render(f'Score : {self.score}',True, pygame.Color("white"))

    def spawn_obstacles(self):
        if not self.timers['obstacle'].active:
            x = WINDOW_WIDTH + randint(100,200)
            y = randint(-600, -200)
            self.obs1 = Obstacle((self.all_sprites,self.collision_sprites),x,y, "ob1")
            y += 680 + 350
            self.obs2 = Obstacle((self.all_sprites,self.collision_sprites),x,y, "ob2")
            self.timers['obstacle'].activate()

    def check_collisions(self, dt):
        for sprite in self.collision_sprites:
            if pygame.sprite.collide_mask(self.player, sprite):
                self.timers['hit'].activate() 
                self.time_active += dt
                Death(self.all_sprites, self.poof_surfs, self.player.rect.midtop)
                self.player.kill()

        if self.player.rect.top >= WINDOW_HEIGHT:
            self.timers['hit'].activate()
            self.time_active += dt
            Fire(self.all_sprites, self.fire_surfs, self.player.rect.midtop)
            self.player.kill()

        for fire_sprite in self.fire_sprites:
            if pygame.sprite.collide_mask(self.player, fire_sprite):
                self.timers['hit'].activate()
                self.time_active += dt
                FirePoof(self.all_sprites, self.firepoof_surfs, self.player.rect.center)
                self.player.kill()


    def draw(self, window):
        window.fill(pygame.Color('black'))
        self.all_sprites.draw(window)
        window.blit(self.score_text, self.score_rect)
        if self.paused:
            window.blit(self.paused_text, self.paused_rect)

    def update(self, dt):
        if not self.paused:
            self.add_score()
            self.persist['score'] = self.score
            self.spawn_obstacles()
            
            if not self.timers['hit'].active:
                self.check_collisions(dt)

            for timer in self.timers.values():
                timer.update()
            self.all_sprites.update(dt)

            if self.time_active > 0:
                self.time_active += dt

            if self.time_active > 15:
                self.done = True
            
            if self.score >= 500 and not self.timers['fireball'].active:
                FireBall((self.all_sprites,self.fire_sprites), self.fireball_surfs)
                #config.SOUNDS['fire'].play()
                self.timers['fireball'].activate()
    
