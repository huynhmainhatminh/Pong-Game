from PodSixNet.Server import Server
from PodSixNet.Channel import Channel
import time

class ClientChannel(Channel):
    def Network(self, data):
        # Nhận dữ liệu từ client
        print("Received:", data)
        self._server.ProcessData(self, data)

class PongServer(Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.players = {}   # {id: channel}
        self.state = {
            "ball": [400, 300],
            "ball_speed": [5, 5],
            "paddles": {0: 300, 1: 300},
            "score": {0: 0, 1: 0}
        }
        self.last_update = time.time()

    def Connected(self, channel, addr):
        print("New connection:", addr)
        pid = len(self.players)
        if pid < 2:
            self.players[pid] = channel
            channel.Send({"action": "set_id", "id": pid})
        else:
            channel.Send({"action": "full"})

    def ProcessData(self, channel, data):
        if data["action"] == "paddle":
            self.state["paddles"][data["id"]] = data["y"]

    def UpdateGame(self):
        # Bóng di chuyển
        self.state["ball"][0] += self.state["ball_speed"][0]
        self.state["ball"][1] += self.state["ball_speed"][1]

        bx, by = self.state["ball"]
        vx, vy = self.state["ball_speed"]

        # --- Va chạm trần/sàn ---
        if by <= 0 or by >= 600:
            self.state["ball_speed"][1] *= -1

        # --- Va chạm paddle trái ---
        # Paddle trái ở x = 50, cao 100, tâm ở self.state["paddles"][0]
        if bx <= 60 and abs(by - self.state["paddles"][0]) <= 50:
            self.state["ball_speed"][0] = abs(vx)  # bật sang phải

        # --- Va chạm paddle phải ---
        # Paddle phải ở x = 740, cao 100, tâm ở self.state["paddles"][1]
        if bx >= 740 and abs(by - self.state["paddles"][1]) <= 50:
            self.state["ball_speed"][0] = -abs(vx)  # bật sang trái

        # --- Kiểm tra bóng ra ngoài (ghi điểm) ---
        if bx <= 0:  # Player 2 ghi điểm
            self.state["score"][1] += 1
            self.state["ball"] = [400, 300]
            self.state["ball_speed"] = [5, 5]
        elif bx >= 800:  # Player 1 ghi điểm
            self.state["score"][0] += 1
            self.state["ball"] = [400, 300]
            self.state["ball_speed"] = [-5, -5]

        # Gửi state cho tất cả client
        for pid, channel in self.players.items():
            channel.Send({"action": "state", "state": self.state})


if __name__ == "__main__":
    server = PongServer(localaddr=("localhost", 1337))
    while True:
        server.Pump()
        server.UpdateGame()
        time.sleep(1/60)
