import pygame
import math

# Объекты
class Ball:
    def __init__(self, x, y, vx, vy, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass

# Создаём два объекта
ball1 = Ball(100, 100, 2, 1, 1)
ball2 = Ball(150, 120, -1, -2, 1)

# Вектор столкновения
collision_vector_x = ball2.x - ball1.x
collision_vector_y = ball2.y - ball1.y

# Угол столкновения
collision_angle = math.atan2(collision_vector_y, collision_vector_x)
collision_angle_degrees = math.degrees(collision_angle)

print(f"Угол столкновения (радианы): {collision_angle}")
print(f"Угол столкновения (градусы): {collision_angle_degrees}")

