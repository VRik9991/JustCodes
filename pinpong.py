import pygame
from classes_pinpong import Platforma,Ball,Kubic


screen = pygame.display.set_mode((800,600))



clock = pygame.time.Clock()
p = Platforma()
b = Ball()
kubiki = [Kubic(0,0),Kubic(80,0),Kubic(160,0),Kubic(240,0),Kubic(320,0),Kubic(400,0),Kubic(480,0),Kubic(560,0),Kubic(640,0),Kubic(720,0),
          Kubic(40,50),Kubic(120,50),Kubic(200,50),Kubic(280,50),Kubic(360,50),Kubic(440,50),Kubic(520,50),Kubic(600,50),Kubic(680,50),
          Kubic(60,100),Kubic(140,100),Kubic(220,100),Kubic(300,100),Kubic(380,100),Kubic(460,100),Kubic(540,100),Kubic(620,100)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    p.display(screen)
    b.display(screen)
    if b.move(p):
        break
    clock.tick(100)
    for kub in kubiki:
        kub.display(screen)
        kub.dead_or_live(b)
        if kub.dead_or_live(b):
            b.colide_with_block(kub)
            kubiki.remove(kub)
    if pygame.key.get_pressed()[pygame.K_a]:
        p.move_left()
    if pygame.key.get_pressed()[pygame.K_d]:
        p.move_right()

    pygame.display.flip()