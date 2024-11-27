import pygame

screen = pygame.display.set_mode((600, 600))
pole = []


class Proletka:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.side = 30
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)

        def Display(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)


with open("pole", "r") as file:
    for i in range(len(file.readlines())):
        pole.append([])
        for j in range(len(file.readline())):
            if file.readline(i)[j] == "X":
                pole[i][-1].append(Proletka(j * 30, i * 30, (255, 255, 255)))
            else:
                pole[i][-1].append(Proletka(j * 30, i * 30, (255, 255, 255)))
# class Cell:
#     def __init__(self, x, y, alive):
#         self.x = x
#         self.y = y
#         self.alive = alive
#         self.side = 30
#         self.color = (255, 255, 255)
#         self.rect = pygame.Rect(self.x, self.y, self.side, self.side)
#
#     def display(self, screen):
#         if self.alive:
#             self.color = (255, 255, 255)
#         else:
#             self.color = (0, 0, 0)
#         pygame.draw.rect(
#             screen,
#             self.color,
#             self.rect
#         )
# x_end = 0
# y_end = 0
# platforma = []
# live = False
# posY = 0
# posX = 0
# empty_field = []
# for i in range(300):
#     platforma.append([])
#     for j in range(300):
#         platforma[-1].append(Cell(posX, posY, live))
#         # live = not live
#         posX += 30
#     # live = not live
#     posX = 0
#     posY += 30
#
# def display(file,platforma):
#     line = 0
#     for i in range(len(file.readlines())):
#
#         for j in range(len(file.readline(line))):
#             stroka = file.readline(line)
#             if stroka[j] == "X":
#                 platforma[i][j].self.alive = True
#         for i in range(30):
#             for j in range(30):
#                 if platforma[i][j].alive:
#                     color = (255, 255, 255)
#                 else:
#                     color = (0, 0, 0)
#                 pygame.draw.rect(
#                     screen,
#                     color,
#                     platforma[i][j].rect
#                 )
running = True
with open("pole", "r") as file:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for i in range(len(pole)):
            for j in range(len(pole[1])):
                pole[i][j].display(screen)
        # display(file,platforma)
