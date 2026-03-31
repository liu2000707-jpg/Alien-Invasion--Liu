import pygame
from pygame.sprite import Sprite, Group

class Bullets(Sprite) :
    bullets_allowed = 10
    color = (0,0,0)
    offset = 0
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen
        self.ship = ship
        self.rect = pygame.Rect(0,0,3,8) #Rect(left,top,width,height)
        self.rect.centerx = ship.rect.centerx - Bullets.offset
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.speed = 0.6

    def draw_bullet(self):
        pygame.draw.rect(self.screen.dimension, Bullets.color, self.rect)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
        #self.draw_bullet()
        if self.rect.bottom <= 0:
            self.kill()






    

   
        
        

    
