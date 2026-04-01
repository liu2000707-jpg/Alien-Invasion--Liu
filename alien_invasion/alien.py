import pygame
from pygame.sprite import Sprite

class Alien(Sprite) :
    alien_width = 50
    alien_height = 45
    def __init__(self, screen, x, y, speed):
        super().__init__()
        self.speed = speed
        self.screen = screen
        self.image = pygame.image.load("D:\\alien_invasion\\images\\alien.bmp")
        self.image = pygame.transform.scale(self.image,(Alien.alien_width,Alien.alien_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)


    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        if self.rect.y > self.screen.dimension.get_rect().height:
            self.kill()

    #def blitme(self):
        #self.screen.dimension.blit(self.image, self.rect)






            
            
            
        
        
        
        
