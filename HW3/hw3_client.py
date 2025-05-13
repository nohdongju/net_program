import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9000))

# 1. Hello 메시지 수신
msg = sock.recv(1024)
print(msg.decode())

# 2. 이름 전송
sock.send('노동주'.encode())

# 3. 학번을 bytes → int로 변환하여 출력
data = sock.recv(4)  # 4바이트 수신
student_id = int.from_bytes(data,'big')
print(student_id)

sock.close()
