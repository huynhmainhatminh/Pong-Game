import pygame
from PodSixNet.Connection import connection, ConnectionListener

class PongClient(ConnectionListener):
    def __init__(self, addr):
        self.Connect(addr)
        self.id = None
        self.state = None

    def Loop(self):
        connection.Pump()
        self.Pump()

    def Network_set_id(self, data):
        self.id = data["id"]
        print("My player ID:", self.id)

        # Đổi tên cửa sổ theo ID
        pygame.display.set_caption(f"Pong Multiplayer - Player {self.id}")

    def Network_state(self, data):
        self.state = data["state"]

    def Network_full(self, data):
        print("Server full!")
        exit()


# --------- GAME LOOP ----------
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong Multiplayer")  # Tạm thời
clock = pygame.time.Clock()
font = pygame.font.SysFont("Courier", 40)

client = PongClient(("localhost", 1337))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if client.state:
        if client.id == 0:   # Player Left
            if keys[pygame.K_w]:
                connection.Send({"action": "paddle", "id": 0, "y": max(50, client.state["paddles"][0] - 7)})
            if keys[pygame.K_s]:
                connection.Send({"action": "paddle", "id": 0, "y": min(550, client.state["paddles"][0] + 7)})
        elif client.id == 1: # Player Right
            if keys[pygame.K_UP]:
                connection.Send({"action": "paddle", "id": 1, "y": max(50, client.state["paddles"][1] - 7)})
            if keys[pygame.K_DOWN]:
                connection.Send({"action": "paddle", "id": 1, "y": min(550, client.state["paddles"][1] + 7)})

    client.Loop()

    # ----- Render -----
    screen.fill((0,0,0))
    if client.state:
        # Ball
        pygame.draw.circle(screen, (255,255,0), client.state["ball"], 10)

        # Paddles
        pygame.draw.rect(screen, (255,0,0), (50, client.state["paddles"][0]-50, 10, 100))   # Paddle left
        pygame.draw.rect(screen, (0,0,255), (740, client.state["paddles"][1]-50, 10, 100)) # Paddle right

        # Score
        score_text = f"{client.state['score'][0]}   {client.state['score'][1]}"
        text_surface = font.render(score_text, True, (255,255,255))
        screen.blit(text_surface, (340, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
