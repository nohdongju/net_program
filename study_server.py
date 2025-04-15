import socket
import sys

port = 9999
BUFSIZE = 1024

if len(sys.argv) > 1:
    port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
s.listen(1)
c, addr = s.accept()
print(addr)

while True:
    data = c.recv(BUFSIZE)
    if not data:
        break
    print('msg: ',data.decode())
    c.send(data)
c.close()