import socket
import json

# Konfiguracja połączenia z serwerem
HOST = '127.0.0.1'  # adres serwera
PORT = 5000         # port serwera

# Przykładowe dane do wysłania
data_to_send = {
    "alarms": [1, 6, 15]
}

# Serializacja do JSON
json_data = json.dumps(data_to_send)

# Utworzenie połączenia TCP i wysłanie danych
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print(f"Połączono z serwerem {HOST}:{PORT}")
        
        s.sendall(json_data.encode())
        print(f"Wysłano dane: {json_data}")

        # Odbiór odpowiedzi od serwera
        response = s.recv(1024).decode()
        print(f"Odpowiedź serwera: {response}")

    except ConnectionRefusedError:
        print("❌ Nie udało się połączyć z serwerem")
    except Exception as e:
        print(f"❌ Błąd: {e}")
