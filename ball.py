import pygame
import random
import math

class Ball(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill("orange")
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.reset(screen_width, screen_height)
        self.max_speed = 10

    def update(self, screen_width, screen_height):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Va chạm trần/sàn
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1

    def bounce(self, paddle):
        # Tính vị trí tương đối của bóng so với paddle
        paddle_center = paddle.rect.centery
        distance = self.rect.centery - paddle_center

        # Chuẩn hóa thành [-1, 1]
        norm = distance / (paddle.rect.height / 2)
        norm = max(-1, min(1, norm))  # giới hạn an toàn

        # Góc lệch tối đa (radians) ~ 45 độ
        max_angle = math.radians(45)
        angle = norm * max_angle

        # Tốc độ giữ nguyên nhưng tăng dần
        speed = math.hypot(self.speed_x, self.speed_y) * 1.1
        speed = min(speed, self.max_speed)

        # Xác định hướng X (trái/phải)
        direction = -1 if self.speed_x > 0 else 1

        # Tính vận tốc mới
        self.speed_x = direction * speed * math.cos(angle)
        self.speed_y = speed * math.sin(angle)

    def reset(self, screen_width, screen_height):
        self.rect.center = [screen_width // 2, screen_height // 2]
        self.speed_x = random.choice([-5, 5])
        self.speed_y = random.choice([-3, 3])
