import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([10, 100])  # Paddle 10x100 px
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.speed = 7

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed

    def move_down(self, screen_height):
        if self.rect.bottom < screen_height:
            self.rect.y += self.speed
