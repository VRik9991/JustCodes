import pygame
from classes_pinpong import Platforma,Ball


screen = pygame.display.set_mode((800,600))



clock = pygame.time.Clock()
p = Platforma()
b = Ball()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    p.display(screen)
    b.display(screen)
    b.move(p)
    clock.tick(100)
    if pygame.key.get_pressed()[pygame.K_a]:
        p.move_left()
    if pygame.key.get_pressed()[pygame.K_d]:
        p.move_right()
    pygame.display.flip()