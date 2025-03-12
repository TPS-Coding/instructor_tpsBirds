import pygame
from .base import BaseState
from settings import *
from .background import BG

class GameOver(BaseState):
    def __init__(self):
        super(GameOver, self).__init__()
        self.title_font = pygame.font.Font(None, 100)
        self.font = pygame.font.Font("font/BD_Cartoon_Shout.ttf", 30)
        self.title = self.title_font.render("GAME OVER", True, pygame.Color('red'))
        self.title_rect = self.title.get_frect(center = self.window_rect.center)
        self.instruction = self.font.render("Click to play again", True, pygame.Color('white'))

        instruction_center = (self.window_rect.center[0], self.window_rect.center[1]+ -150)
        self.instruction_rect = self.instruction.get_frect(center = instruction_center)

        ## Sprite Group
        self.all_sprites = pygame.sprite.Group()
        ## Sprite
        self.bg = BG(self.all_sprites)

    def startup(self, persistent):
        score = persistent["score"]
        self.final_score = self.font.render(f"Final Score: {score}",True, 'white')
        score_center = (self.window_rect.center[0], self.window_rect.center[1] + 50)
        self.score_rect = self.final_score.get_frect(center = score_center)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.next_state = "GAMEPLAY"
            self.done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit = True
    
    
    def draw(self, window):
        window.fill(pygame.Color('black'))
        self.all_sprites.draw(window)
        window.blit(self.title, self.title_rect)
        window.blit(self.final_score, self.score_rect)
        window.blit(self.instruction, self.instruction_rect)

    def update(self, dt):
        self.all_sprites.update(dt)

        

        
