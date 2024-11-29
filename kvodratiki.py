import pygame
import random

screen = pygame.display.set_mode((800, 600))


class Kubik:
    def __init__(self):
        self.y = 400
        self.x = 300
        self.side = 10

        self.vay_x = 1 * random.randint(-1,1)
        self.vay_y = 1 * random.randint(-1,1)
        self.rect = pygame.Rect(self.y, self.x, self.side, self.side)
        self.count = 0

    def display(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def move(self):
        self.count +=1
        self.y += self.vay_y
        self.x += self.vay_x
        self.rect = pygame.Rect(self.y, self.x, self.side, self.side)
        if self.x <= 0:
            self.vay_x = 1
        if self.x >= 590:
            self.vay_x = -1
        if self.y >= 790:
            self.vay_y = -1
        if self.y <= 0:
            self.vay_y = 1
    def clone(self,masiv):
        if self.count == 1000:
            masiv.append(Kubik())
            self.count = 0


kubiki = [Kubik()]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for kubik in kubiki:
        kubik.move()
        kubik.display(screen)
        kubik.clone(kubiki)
    pygame.display.flip()
