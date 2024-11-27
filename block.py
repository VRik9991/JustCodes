import pygame
import sys

# инициализация Pygame
pygame.init()

# установка размера окна
screen = pygame.display.set_mode((800, 600))

# загрузка изображений
player_img = pygame.image.load('player.png')
bullet_img = pygame.image.load('bullet.png')

player_pos = [400, 300]
bullets = []

# главный цикл игры
while True:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append([event.pos[0] - 50, event.pos[1] - 50])

    screen.fill((0, 0, 0))

    # отрисовка игрока
    screen.blit(player_img, player_pos)

    # отрисовка пуль
    for bullet in bullets:
        screen.blit(bullet_img, bullet)

    pygame.display.flip()
