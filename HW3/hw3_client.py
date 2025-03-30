import socket
sock = socket.socket(socket.AF_INET,
 socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
# 본인의 이름을 문자열로 전송
name = "Dongju Noh"
sock.send(name.encode())
# 본인의 학번을 수신 후 출력
name_id = sock.recv(1024)
print(name_id.decode())

sock.close()