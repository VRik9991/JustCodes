import time

import pygame


class Platforma:
    def __init__(self):
        self.coordinate = 250
        self.rect = pygame.Rect(self.coordinate, 580, 250, 20)

    def display(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def move_left(self, ):
        if self.coordinate <= 0:
            self.coordinate += 1
        else:
            self.coordinate -= 1
        self.rect = pygame.Rect(self.coordinate, 580, 250, 20)

    def move_right(self, ):
        if self.coordinate + 250 >= 800:
            self.coordinate -= 1
        else:
            self.coordinate += 1
        self.rect = pygame.Rect(self.coordinate, 580, 250, 20)


class Ball:
    def __init__(self):
        self.explosion_pic = pygame.image.load('ball.png')
        self.x_and_y = [400, 300]
        self.side = 10
        self.way = [2, -2]
        self.rect = pygame.Rect(self.x_and_y[0], self.x_and_y[1], self.side, self.side)

    def display(self, screen):
        # pygame.draw.rect(screen, (255, 255, 255), self.rect)
        screen.blit(self.explosion_pic, self.rect)

    def move(self, platforma):
        self.x_and_y[0] += self.way[0]
        self.x_and_y[1] += self.way[1]
        if self.x_and_y[0] <= 0:
            self.way[0] = 2
        if self.x_and_y[0] + self.side >= 800:
            self.way[0] = -2
        if self.x_and_y[1] <= 0:
            self.way[1] = 2
        if self.x_and_y[1] + self.side >= 600:
            return True
        if self.rect.colliderect(platforma.rect):
            self.way[1] = -2
        self.rect = pygame.Rect(self.x_and_y[0], self.x_and_y[1], self.side, self.side)

    def colide_with_block(self, kub):
        if kub.dead == False:

            if self.rect.colliderect(kub.rect):
                if self.x_and_y[0] + 5 < kub.x + 30:
                    self.way[0] = -2
                if self.x_and_y[0] + 5 > kub.x + 30:
                    self.way[0] = 2
                if self.x_and_y[1] + 5 < kub.y + 15:
                    self.way[1] = -2
                if self.x_and_y[1] + 5 > kub.y + 15:
                    self.way[1] = 2


class Kubic:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dead = False
        self.rect = pygame.Rect(self.x, self.y, 60, 30)
        self.color = (255, 255, 255)
        self.explosion = [pygame.image.load(f'{i}.png') for i in range(1,11)]
        for i in range(1, 11): self.explosion.append(pygame.image.load(str(i) + '.png'))
        self.image_numer = 0

        self.animation_frame = 0

    def display(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    def explode(self,screen):

        self.animation_frame +=1
        if self.animation_frame == 10:
            self.animation_frame = 0
            self.image_numer += 1
            if self.image_numer == 10:
                return True
        screen.blit(self.explosion[self.image_numer], self.rect)

    def dead_or_live(self, ball,screen):
        if self.rect.colliderect(ball.rect):
            self.dead = True
        if self.dead:
            # self.explode(screen)
            return self.explode(screen)





