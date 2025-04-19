import socket

SERVER_PORT = 9999
BUFFER = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('Enter the message("send mboxID message" or "receive mboxID"):')

    s.sendto(msg.encode(), ('localhost', SERVER_PORT))

    if msg == 'quit':
        break

    data, _ = s.recvfrom(BUFFER)
    print(data.decode())

s.close()
