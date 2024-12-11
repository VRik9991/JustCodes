import time

import pygame
import random

screen = pygame.display.set_mode((800, 600))


class Tocki:
    def __init__(self):
        self.vse_tockiorigin = [[400, 0], [790, 590], [0, 590]]
        self.vse_tockinovi = []
        self.vse_tockinovi.append([random.randint(10,780),random.randint(10,580)])

    def display(self, screen):
        for tocka in self.vse_tockinovi:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(tocka[0], tocka[1], 1, 1))
        for tocka in self.vse_tockiorigin:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(tocka[0], tocka[1], 1, 1))

    def create_tocka(self):
        for i in range(1):
            A = self.vse_tockinovi[-1]
            B = self.vse_tockiorigin[random.randint(0, len(self.vse_tockiorigin) - 1)]
            while A == B:
                B = self.vse_tockiorigin[random.randint(0, len(self.vse_tockiorigin) - 1)]
            self.vse_tockinovi.append([int(A[0] / 2 + B[0] / 2), int(A[1] / 2 + B[1] / 2)])


#         както та будет А\2 + В\2


running = True
kub = Tocki()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    kub.display(screen)
    kub.create_tocka()
    pygame.display.flip()
