import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill("orange")
        self.rect = self.image.get_rect()
        self.rect.center = [screen_width//2, screen_height//2]
        self.speed_x = random.choice([-5, 5])
        self.speed_y = random.choice([-5, 5])
        self.speed_increment = 1.05
        self.max_speed = 12

    def update(self, screen_width, screen_height):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Va chạm trần/sàn
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1

    def bounce(self):
        self.speed_x = -self.speed_x
        if abs(self.speed_x) < self.max_speed:
            self.speed_x = int(self.speed_x * self.speed_increment)
        if abs(self.speed_y) < self.max_speed:
            self.speed_y = int(self.speed_y * self.speed_increment)

    def reset(self, screen_width, screen_height):
        self.rect.center = [screen_width//2, screen_height//2]
        self.speed_x *= -1
        self.speed_y = random.choice([-5, 5])
