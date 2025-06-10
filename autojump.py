from pythonosc.udp_client import SimpleUDPClient
import time

# === 送信先設定 ===
ip = "127.0.0.1"       # 通常はローカルホスト
port = 9000            # VRChatの受信用ポート（デフォルト：9000）

# === OSCクライアント生成 ===
client = SimpleUDPClient(ip, port)

# === パラメータ送信関数 ===
def send_osc_parameter(parameter_name, value):
    address = f"/input/Jump"
    client.send_message(address, value)
    print(f"Sent {value} to {address}")

# === 使用例 ===
while True:
    send_osc_parameter("Jump", True)
    time.sleep(1)  # 一瞬だけTrue（短くしすぎると反応しないことがある）
    send_osc_parameter("Jump", False)
    print("Jump signal sent. Waiting 70 seconds...")
    time.sleep(70)
