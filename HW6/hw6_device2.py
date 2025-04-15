import socket
import random

PORT = 9002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(1)

conn, addr = s.accept()
print("Device 2 연결됨:", addr)

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    if data == 'Request':
        heartbeat = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)
        response = f'{heartbeat},{steps},{cal}'
        conn.send(response.encode())
    elif data == 'quit':
        print("Device 2 종료")
        break

conn.close()
s.close()
