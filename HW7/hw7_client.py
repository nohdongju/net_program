from socket import *

port = 3333
BUFFSIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message ("send mboxId message" or "receive mboxId "): ')

    sock.sendto(msg.encode(), ('localhost', port))

    if msg == 'quit':
        break

    data, addr = sock.recvfrom(BUFFSIZE)
    print(data.decode())

sock.close()
