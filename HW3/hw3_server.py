import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from', addr)

    # 1. Hello 메시지 전송
    client.send(b'Hello ' + addr[0].encode())

    # 2. 이름 수신
    name = client.recv(1024).decode()
    print(name)

    # 3. 학번을 int → bytes로 변환하여 전송
    student_id = 20221300
    byte_data = student_id.to_bytes(4,'big')
    client.send(byte_data)

    client.close()
