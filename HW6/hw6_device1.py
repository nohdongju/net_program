import socket
import random

PORT = 9001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(1)

conn, addr = s.accept()
print("Device 1 연결됨:", addr)

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    if data == 'Request':
        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        illum = random.randint(70, 150)
        response = f'{temp},{humid},{illum}'
        conn.send(response.encode())
    elif data == 'quit':
        print("Device 1 종료")
        break

conn.close()
s.close()
