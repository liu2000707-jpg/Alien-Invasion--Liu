from ship import Ship
from bullets import Bullets
from pygame.sprite import Group

class Settings:
    def __init__(self, screen):
        self.screen = screen
        self.ship = Ship(self.screen)
        self.ships = Group()
        self.ships_left = 3
        self.prep_ships()
    def prep_ships(self):
        self.ships.empty()
        for ship_number in range(self.ships_left):
            ship = Ship(self.screen)
            ship.rect.x = ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    def show_ships_left(self):
        self.ships.draw(self.screen.dimension)


    def ship_level_up(self, bullets, scores, time, ls_ship):
        if scores <60:
            self.ship_level = 1
        if scores >= 60:
            self.ship_level = 2
        if scores >= 180:
            self.ship_level = 3
        if scores >= 300:
            self.ship_level = 4
        ls_ship = self.auto_fire_ship(bullets, time, ls_ship)
        return ls_ship

    def auto_fire_ship(self, bullets, time, ls_ship):
        shoot_delay = time - ls_ship
        if self.ship_level == 1:
            Bullets.bullets_allowed = 10
            if shoot_delay >= 300:
                Bullets.color = (0, 0, 0)
                Bullets.offset = 0
                new_bullet = Bullets(self.screen, self.ship)
                bullets.add(new_bullet)
                ls_ship = time
        elif self.ship_level == 2:
            if shoot_delay >= 200:
                Bullets.bullets_allowed = 20
                Bullets.color = (0, 100, 0)
                Bullets.offset = 4
                bullet_left = Bullets(self.screen, self.ship)
                bullets.add(bullet_left)
                Bullets.offset = -4
                bullet_right = Bullets(self.screen, self.ship)
                bullets.add(bullet_right)
                ls_ship = time
        elif self.ship_level == 3:
            if shoot_delay >= 150:
                Bullets.bullets_allowed = 26
                Bullets.color = (0, 50, 150)
                Bullets.offset = 4
                bullet_left = Bullets(self.screen, self.ship)
                bullets.add(bullet_left)
                Bullets.offset = -4
                bullet_right = Bullets(self.screen, self.ship)
                bullets.add(bullet_right)
                ls_ship = time
        elif self.ship_level == 4:
            Bullets.bullets_allowed = 30
            if shoot_delay >= 100:
                Bullets.color = (153, 50, 204)
                Bullets.offset = 0
                new_bullet = Bullets(self.screen, self.ship)
                bullets.add(new_bullet)
                Bullets.offset = 6
                bullet_left = Bullets(self.screen, self.ship)
                bullets.add(bullet_left)
                Bullets.offset = -6
                bullet_right = Bullets(self.screen, self.ship)
                bullets.add(bullet_right)
                ls_ship = time
        return ls_ship













