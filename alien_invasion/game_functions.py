import pygame
import math
import time
import sys
import random
from random import randint
from alien import Alien
from elitealien import EliteAlien
from kingalien import KingAlien
from ea_bullets import EA_Bullets
from ka_bullets import KA_Bullets
from stats import Stats
from gameaudios import GameAudios
last_trigger_scores = 0
audios = GameAudios()

def check_events(events_list, ship, screen, play_button, stats, sb, settings):
    for event in events_list :
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                audios.play_bgm("battle")
                KingAlien.Yking_spawned = False
                KingAlien.Oking_spawned = False
                KingAlien.Rking_spawned = False
                stats.scores = 0
                settings.ships_left = 3
                sb.prep_score()
                stats.game_active = True
                pygame.mouse.set_visible(False)

        if event.type == pygame.QUIT:
            stats.save_high_score()
            pygame.time.delay(50)
            pygame.quit()
            sys.exit()

        if stats.game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False

def create_kingalien(kingalien, screen, type, aliens):
    aliens.empty()
    x = screen.dimension.get_rect().centerx
    boss = KingAlien(screen, x, type)
    kingalien.add(boss)

def create_fleets(screen, alien_last_y, scores, kingalien, aliens, elitealiens, settings):
    global last_trigger_scores
    if settings.ship_level > 1:
        if scores % 60 == 0 and scores != 0 and scores != last_trigger_scores:
            EliteAlien.elitealiens_spawned = True
    if EliteAlien.elitealiens_spawned and alien_last_y >= 250:
        x = 50
        direction = 1
        elitealien = EliteAlien(screen, x, direction)
        elitealiens.add(elitealien)
        x = 1150
        direction = -1
        elitealien = EliteAlien(screen, x, direction)
        elitealiens.add(elitealien)
        last_trigger_scores = scores
        alien_last_y = 0
        EliteAlien.elitealiens_spawned = False
    if settings.ship_level == 4:
        if not KingAlien.Yking_spawned :
            type = "yellow"
            create_kingalien(kingalien, screen, type, aliens)
            KingAlien.Yking_spawned = True
            audios.play_bgm("boss")
        elif not kingalien:
            if not KingAlien.Oking_spawned:
                type = "orange"
                create_kingalien(kingalien, screen, type)
                KingAlien.Oking_spawned = True
            elif not KingAlien.Rking_spawned:
                type = "red"
                create_kingalien(kingalien, screen, type)
                KingAlien.Rking_spawned = True
    if alien_last_y >= 250:
        if settings.ship_level == 1:
            speed = 0.02
        elif settings.ship_level == 2:
            speed = 0.03
        elif settings.ship_level == 3:
            speed = 0.045
        else:
            speed = 0.06
        if not elitealiens:
            y = 0
            x = 0
            while x < 850:
                x = x + Alien.alien_width + randint(50, 250)
                if not kingalien:
                    alien = Alien(screen, x, y, speed)
                    aliens.add(alien)
                    alien_last_y = 0
                else:
                    if not (450 <= x <= 670):
                        alien = Alien(screen, x, y, speed)
                        aliens.add(alien)
                        alien_last_y = 0
    return alien_last_y

def refresh_all_sprites(stats, play_button, aliens, ship_group, screen, sb, kingalien, elitealiens, settings,  *groups):
    screen.full_screen()
    if not stats.game_active:
        play_button.draw_button()

    else:
        aliens.update()
        aliens.draw(screen.dimension)
        elitealiens.update()
        elitealiens.draw(screen.dimension)
        ship_group.update()
        ship_group.draw(screen.dimension)
        sb.show_score()
        settings.show_ships_left()
        kingalien.update()
        kingalien.draw(screen.dimension)
        for boss in kingalien:
            boss.draw_KA_HP()

        for group in groups:
            for bullet in group:
                bullet.update()
                bullet.draw_bullet()

def create_KEA_bullet(screen, elitealiens, ea_bullets, ea_last_shoot, ka_last_shoot, time, kingalien):
    ea_shoot_delay = time - ea_last_shoot
    ka_shoot_delay = time - ka_last_shoot
    if ea_shoot_delay >= 1000 and elitealiens:
        for elitealien in elitealiens:
            bullet = EA_Bullets(screen, elitealien)
            ea_bullets.add(bullet)
            ea_last_shoot = time
    if ka_shoot_delay >= 3000 and kingalien:
        for boss in kingalien:
            boss.get_angle()
            theta = boss.angle
            while (boss.angle <= theta <= (math.pi - boss.angle)):
                bullet = KA_Bullets(screen, boss, theta)
                ea_bullets.add(bullet)
                theta = theta + random.uniform(0.2, 0.6)
                ka_last_shoot = time
    return  ea_last_shoot, ka_last_shoot

def boss_control(kingalien):
    for boss in kingalien:
        if boss.HP <= boss.max_HP and boss.HP >= 400:
            boss.king_state = "show"
        elif boss.HP <= 400 and boss.HP >= 200:
            boss.king_state = "forward"
        elif boss.HP <= 200 and boss.HP > 0:
            boss.king_state = "backward"
        elif boss.HP <= 0:
            kingalien.empty()

def check_collisions(screen, aliens, bullets_player, bullets_aliens, ship_group, alien_last_y, stats, kingalien, elitealiens, sb, ships_left):
    collisions1 = pygame.sprite.groupcollide(bullets_player, aliens, True, True)
    collisions4 = pygame.sprite.groupcollide(kingalien, bullets_player, False, True)
    collisions5 = pygame.sprite.groupcollide(bullets_player, elitealiens, True, True)
    last_collision1 = False
    last_collision5 = False
    last_collision1 = collisions1
    last_collision5 = collisions5
    scores_record(stats, sb, collisions1, collisions5)
    for ship in ship_group:
        collisions2 = pygame.sprite.spritecollideany(ship, bullets_aliens)
        collisions3 = pygame.sprite.spritecollideany(ship, aliens)
        collisions6 = pygame.sprite.spritecollide(ship, kingalien, True)

    alien_check_y = False
    for alien in aliens:
        if alien.rect.bottom >= screen.dimension.get_rect().bottom:
            alien_check_y = True
    boss_check_y = False
    for boss in kingalien:
        if boss.rect.bottom >= screen.dimension.get_rect().bottom:
            boss_check_y = True

    if collisions2 or collisions3 or alien_check_y or KingAlien.went_off or EliteAlien.went_off:
        ship_hit(stats, screen, alien_last_y, stats.scores, ship_group, aliens, bullets_player, bullets_aliens, kingalien, elitealiens, sb, ships_left)
        alien_check_y = False
        EliteAlien.went_off = False

    if collisions6 or boss_check_y :
        stats.game_active = False

    if collisions4 :
        for boss in kingalien:
            boss.HP -= 1
            boss_control(kingalien)
    return collisions1, collisions5

def scores_record(stats, sb, *groups):
    for group in groups:
        for bullet, hit_aliens in group.items():
            for alien in hit_aliens:
                if isinstance(alien, Alien):
                    stats.scores += 2
                    sb.prep_score()
                if isinstance(alien, EliteAlien):
                    stats.scores += 4
                    sb.prep_score()
    if stats.scores > stats.high_score:
        stats.high_score = stats.scores
        sb.prep_high_score()
    #print(scores)

def ship_hit(stats, screen, alien_last_y, scores, ship_group, aliens, bullets_player, bullets_aliens, kingalien, elitealiens, sb, settings):
    time.sleep(0.5)
    if settings.ships_left > 0:
        settings.ships_left -= 1
        settings.prep_ships()
        aliens.empty()
        elitealiens.empty()
        bullets_player.empty()
        bullets_aliens.empty()

        pygame.display.flip()
    elif settings.ships_left <= 0:
        audios.stop_bgm()
        kingalien.empty()
        KingAlien.king_spawned = True
        stats.game_active = False
        pygame.mouse.set_visible(True)


















