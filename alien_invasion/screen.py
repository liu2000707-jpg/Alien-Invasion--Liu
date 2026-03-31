import pygame

class Screen:
    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 750
        self.dimension = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.title = pygame.display.set_caption("Alien Invasion")
        self.bg_color = (220, 220, 220)
    
    def full_screen(self ) :
        self.dimension.fill(self.bg_color)
        
    
