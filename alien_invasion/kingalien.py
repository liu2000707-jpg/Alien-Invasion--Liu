from alien import Alien
import pygame
import math
class KingAlien(Alien):
    Yking_spawned = False
    Oking_spawned = False
    Rking_spawned = False
    KA_HP_spawned = False
    went_off = False
    KA_HP_width = 0
    KA_HP_height = 0
    def __init__(self, screen, x, type):
        super().__init__(screen, x, y=0, speed=0.003)
        self.type = type
        self.king_state = "show"
        self.KA_HP_width, self.KA_HP_height = 150, 10
        self.KA_HP_color1 = (204, 0, 0)
        self.KA_HP_color2 = (0, 204, 0)
        self.KA_HP_radius = 5
        self.load_images()
        self.image = pygame.transform.scale(self.image, (150, 140))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.HP = self.max_HP


    def load_images(self):
        if self.type == "yellow":
            self.image = pygame.image.load('images/kingalien1.bmp')
            self.max_HP = 500
        elif self.type == "orange":
            self.image = pygame.image.load('images/kingalien2.bmp')
            self.max_HP = 500
        elif self.type == "red":
            self.image = pygame.image.load('images/kingalien3.bmp')
            self.max_HP = 500

    def draw_KA_HP(self):
        self.KA_HP_fill_width = self.KA_HP_width * (self.HP / self.max_HP)
        self.KA_HP_bg_rect = pygame.Rect(self.rect.x - 10, self.rect.y, self.KA_HP_width, self.KA_HP_height)
        pygame.draw.rect(self.screen.dimension, self.KA_HP_color1, self.KA_HP_bg_rect)
        self.KA_HP_fill_rect = pygame.Rect(self.rect.x - 10, self.rect.y, self.KA_HP_fill_width, self.KA_HP_height)
        pygame.draw.rect(self.screen.dimension, self.KA_HP_color2, self.KA_HP_fill_rect)


    def update(self):
        if self.king_state == "show":
            self.rect.y = 0
        elif self.king_state == "forward":
            self.y += self.speed
            self.rect.y = self.y
        elif self.king_state == "backward":
            self.y -= self.speed
            self.rect.y = self.y
        if self.rect.y < 0 or self.rect.y > 800:
            KingAlien.went_off = True
            self.kill()

    def get_angle(self):
        tan_value = self.screen.screen_width / (2 * (self.screen.screen_height - self.rect.bottom))
        self.angle = math.pi / 2 - math.atan(tan_value)





            
            
        
            
            
        
    
