from alien import Alien
import pygame
class EliteAlien(Alien):
    elitealiens_spawned = False
    went_off = False
    def __init__(self, screen, x, direction):
        super().__init__(screen, x, y=150, speed = 0.05)
        self.image = pygame.image.load('images/elitealien.bmp')
        self.image = pygame.transform.scale(self.image, (55,50))
        self.direction = direction


    def update(self):
        self.x += self.speed * self.direction
        self.rect.x = self.x
        if self.rect.x <= 0 or self.rect.x >=1250:
            EliteAlien.went_off = True
            self.kill()










        

        
    
        
