import pygame
import sys
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("D:\\alien_invasion\\images\\spaceship.bmp")
        self.image = pygame.transform.scale(self.image, (45,30))
        self.rect = self.image.get_rect()         #飞船矩形
        self.screen_rect = screen.dimension.get_rect()    #获取屏幕外接矩形
        self.speed = 0.3
        self.moving_right = False
        self.moving_left = False
     
        
        self.rect.centerx = float(self.screen_rect.centerx)        #屏幕中线
        self.x = float(self.rect.x)
        self.rect.bottom = self.screen_rect.bottom      #屏幕底部

    def update(self):
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x += self.speed
                
        if self.moving_left and self.rect.left >= self.screen_rect.left:
            self.x -= self.speed
        self.rect.centerx = self.x
        
