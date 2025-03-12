import pygame
from .base import BaseState
from .button import Button

WINDOW_WIDTH, WINDOW_HEIGHT = 600, 800

class Menu(BaseState):
    def __init__(self):
        super(Menu, self).__init__()
        self.title_font = pygame.font.Font("font/BD_Cartoon_Shout.ttf", 60)
        self.title = self.title_font.render("TPS BIRDS", True, pygame.Color('red'))
        self.title_rect = self.title.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT*0.3))
        self.next_state = "GAMEPLAY"

        self.bg_image = pygame.image.load("graphics/backgrounds/1.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.bg_rect = self.bg_image.get_frect(topleft = (0,0))

        ## Button
        self.button_surf = pygame.image.load("graphics/UI/Continue.png").convert_alpha()
        self.button_pos = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
        self.play_button = Button(self.button_surf, self.button_pos)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_button.check_click() == True:
                self.done = True

    def draw(self, window):
        window.blit(self.bg_image, self.bg_rect)
        window.blit(self.title, self.title_rect)
        self.play_button.draw()