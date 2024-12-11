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
        self.x_and_y = [400, 300]
        self.side = 10
        self.way = [2,-2 ]
        self.rect = pygame.Rect(self.x_and_y[0], self.x_and_y[1], self.side, self.side)

    def display(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

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
            self.way[1] = -2
        if self.rect.colliderect(platforma.rect):
            self.way[1] = -2
        self.rect = pygame.Rect(self.x_and_y[0], self.x_and_y[1], self.side, self.side)
