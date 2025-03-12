import pygame

class Button:
    def __init__(self,surf,pos,enabled=True):

        self.image = surf
        self.rect = self.image.get_frect(center = (pos))
        self.enabled = enabled

        self.display_surface = pygame.display.get_surface()
        
        self.draw()

    def draw(self):
        if self.enabled:
            self.display_surface.blit(self.image, self.rect)


    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0] ## 0 index for the left click
        if left_click and self.rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False


        

