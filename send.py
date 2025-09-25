import socket
import json

HOST = '127.0.0.1'
PORT = 5000

data_to_send = {"alarms": [2, 2, 15]}
json_data = json.dumps(data_to_send)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        s.sendall(json_data.encode())
        s.shutdown(socket.SHUT_WR)  # ✅ kończymy wysyłanie
        response = s.recv(1024).decode()
        print("Odpowiedź serwera:", response)
    except Exception as e:
        print("Błąd klienta:", e)