import pygame
import random

# 初始化
pygame.init()
screen = pygame.display.set_mode((480, 600))
pygame.display.set_caption("外星入侵")
clock = pygame.time.Clock()

# 颜色
WHITE = (255,255,255)
BLUE  = (0,0,255)
RED   = (255,0,0)
GREEN = (0,255,0)

# 玩家
player_x = 200
player_y = 500
player_speed = 5

# 子弹
bullets = []
bullet_speed = 7

# 外星人
aliens = []
for i in range(5):
    aliens.append([random.randint(0, 430), random.randint(-300, 0)])

# 主循环
running = True
while running:
    screen.fill((0,0,0))

    # 事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + 15, player_y])

    # 玩家移动
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 450:
        player_x += player_speed

    # 绘制玩家
    pygame.draw.rect(screen, BLUE, (player_x, player_y, 30, 30))

    # 子弹移动
    for b in bullets[:]:
        b[1] -= bullet_speed
        pygame.draw.rect(screen, GREEN, (b[0], b[1], 4, 10))
        if b[1] < 0:
            bullets.remove(b)

    # 外星人移动
    for a in aliens[:]:
        a[1] += 2
        pygame.draw.rect(screen, RED, (a[0], a[1], 40, 30))

        # 碰撞：子弹打外星人
        for b in bullets[:]:
            if a[0] < b[0] < a[0]+40 and a[1] < b[1] < a[1]+30:
                aliens.remove(a)
                bullets.remove(b)
                aliens.append([random.randint(0,430), random.randint(-300,0)])

        # 外星人到底部
        if a[1] > 600:
            aliens.remove(a)
            aliens.append([random.randint(0,430), -50])

    pygame.display.update()
    clock.tick(60)

pygame.quit()