from socket import *
port = 3333
BUFFSIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

msgbox = {}

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    msg = data.decode()
    lst = msg.split(' ',2)

    if lst[0] == 'send':
        mboxId, message = lst[1], lst[2]
        if mboxId not in msgbox:
            msgbox[mboxId] = []
        msgbox[mboxId].append(message)
        sock.sendto(b'OK', addr)
    elif lst[0] == 'receive':
        mboxId = lst[1]
        if mboxId in msgbox and msgbox[mboxId]:
            response = msgbox[mboxId].pop(0)
            sock.sendto(response.encode(), addr)
        else:
            sock.sendto(b'No messages',addr)
sock.close()