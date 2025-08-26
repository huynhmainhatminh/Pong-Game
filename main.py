import pygame
import sys
from paddle import Paddle
from ball import Ball
from score import Score

pygame.init()

# Màn hình
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONG - PyGame Edition")
clock = pygame.time.Clock()

# Nhập tên người chơi (console input)
left_player = input("Enter name for Left Player (W/S): ") or "Left Player"
right_player = input("Enter name for Right Player (Up/Down): ") or "Right Player"

# Paddle & Ball
left_paddle = Paddle(50, SCREEN_HEIGHT//2, "yellow")
right_paddle = Paddle(SCREEN_WIDTH-50, SCREEN_HEIGHT//2, "red")
ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)

# Nhóm sprite
all_sprites = pygame.sprite.Group()
all_sprites.add(left_paddle, right_paddle, ball)

# Score
score = Score(left_player, right_player)

# Vẽ line giữa sân
def draw_center_line():
    for y in range(0, SCREEN_HEIGHT, 40):
        pygame.draw.rect(screen, (255,255,255), (SCREEN_WIDTH//2 - 2, y, 4, 20))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.move_up()
    if keys[pygame.K_s]:
        left_paddle.move_down(SCREEN_HEIGHT)
    if keys[pygame.K_UP]:
        right_paddle.move_up()
    if keys[pygame.K_DOWN]:
        right_paddle.move_down(SCREEN_HEIGHT)

    # Update ball
    ball.update(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Kiểm tra va chạm paddle
    if pygame.sprite.collide_rect(ball, left_paddle) and ball.speed_x < 0:
        ball.bounce(left_paddle)
    if pygame.sprite.collide_rect(ball, right_paddle) and ball.speed_x > 0:
        ball.bounce(right_paddle)

    # Kiểm tra điểm
    if ball.rect.left <= 0:
        score.add_right()
        ball.reset(SCREEN_WIDTH, SCREEN_HEIGHT)
    if ball.rect.right >= SCREEN_WIDTH:
        score.add_left()
        ball.reset(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Vẽ
    screen.fill("black")
    draw_center_line()
    all_sprites.draw(screen)
    score.draw(screen, SCREEN_WIDTH)

    # Kiểm tra thắng
    winner = score.check_winner()
    if winner:
        font = pygame.font.SysFont("Courier", 50, bold=True)
        text = font.render(winner, True, (255, 255, 0))
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
