import pygame
import math
from ea_bullets import EA_Bullets

class KA_Bullets(EA_Bullets):
    def __init__(self, screen, kingalien, theta):
        super().__init__(screen, elitealien = kingalien)
        self.theta = theta
        self.Vx = self.speed * math.cos(self.theta)
        self.Vy = self.speed * math.sin(self.theta)

    def update(self):
        self.x += self.Vx
        self.rect.x = self.x
        self.y += self.Vy
        self.rect.y = self.y
        if self.rect.bottom >= self.screen.dimension.get_rect().bottom:
            self.kill()
        
        
        
    


        
        
        
