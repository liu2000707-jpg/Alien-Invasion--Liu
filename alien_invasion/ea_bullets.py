import pygame
from pygame.sprite import Sprite
class EA_Bullets(Sprite):
    def __init__(self, screen, elitealien):
        super().__init__()
        self.screen = screen
        self.elitealien = elitealien
        self.radius = 3
        self.color = (255,0,0)
        self.speed = 0.15
        
        self.size = 2 * self.radius
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = elitealien.rect.centerx
        self.rect.top = elitealien.rect.bottom
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        
        
    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        if self.rect.bottom >= self.screen.dimension.get_rect().bottom:
            self.kill()
    
    def draw_bullet(self):
        pygame.draw.circle(self.screen.dimension, self.color, self.rect.center, self.radius)
