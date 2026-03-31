import pygame
from settings import Settings
from bullets import Group
from screen import Screen
from scoreboard import Scoreboard
from stats import Stats
from button import Button
import game_functions as gf


class Game():
    def __init__(self):
        pygame.init()
        self.screen = Screen()

        self.ship_group = Group()
        self.settings = Settings(self.screen)
        self.ship_group.add(self.settings.ship)

        self.bullets_player = Group()
        self.ls_ship = 0
        self.bullets_aliens = Group()
        self.aliens = Group()
        self.alien_last_y = 0
        self.elitealiens = Group()
        self.kingalien = Group()

        self.stats = Stats()
        self.sb = Scoreboard(self.screen, self.stats)
        self.play_button = Button(self.screen, "Play")

        self.time = 0
        self.ea_last_shoot = 0
        self.ka_last_shoot = 0

    def run_game(self):
        while True:
            self.time = pygame.time.get_ticks()
            self.alien_last_y += 0.05
            self.handle_events = []

            for event in pygame.event.get():
                self.handle_events.append(event)
            gf.check_events(self.handle_events, self.settings.ship, self.screen, self.play_button, self.stats, self.sb, self.settings)
            if self.stats.game_active:
                self.alien_last_y = gf.create_fleets(self.screen, self.alien_last_y, self.stats.scores, self.kingalien, self.aliens, self.elitealiens)
                self.ea_last_shoot, self.ka_last_shoot = gf.create_KEA_bullet(self.screen, self.elitealiens, self.bullets_aliens, self.ea_last_shoot, self.ka_last_shoot, self.time, self.kingalien)
                self.ls_ship = self.settings.ship_level_up( self.bullets_player, self.stats.scores, self.time, self.ls_ship)
                gf.check_collisions(self.screen, self.aliens, self.bullets_player, self.bullets_aliens, self.ship_group, self.alien_last_y, self.stats, self.kingalien, self.elitealiens, self.sb, self.settings)
                #print(f"子弹：{len(self.bullets_player):<4}  外星人：{len(self.aliens)}")
            gf.refresh_all_sprites(self.stats, self.play_button, self.aliens, self.ship_group, self.screen, self.sb, self.kingalien,  self.elitealiens, self.settings, self.bullets_player, self.bullets_aliens)
            pygame.display.flip()







    
