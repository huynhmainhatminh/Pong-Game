import pygame

class Score:
    def __init__(self, left_name, right_name):
        self.left_score = 0
        self.right_score = 0
        self.left_name = left_name
        self.right_name = right_name
        self.font = pygame.font.SysFont("Courier", 40)

    def draw(self, screen, screen_width):
        left_text = self.font.render(f"{self.left_name}: {self.left_score}", True, (255,255,255))
        right_text = self.font.render(f"{self.right_name}: {self.right_score}", True, (255,255,255))

        screen.blit(left_text, (50, 20))
        screen.blit(right_text, (screen_width - right_text.get_width() - 50, 20))

    def add_left(self):
        self.left_score += 1

    def add_right(self):
        self.right_score += 1

    def check_winner(self):
        if self.left_score >= 10:
            return f"{self.left_name} Wins!"
        elif self.right_score >= 10:
            return f"{self.right_name} Wins!"
        return None
