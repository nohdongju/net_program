import socket

PORT = 9999
BUFFER = 1024

# 메시지 저장소 (mboxID: queue of messages)
mailbox = {}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', PORT))

print("Listening...")

while True:
    data, addr = s.recvfrom(BUFFER)
    msg = data.decode()

    if msg == 'quit':
        print("종료")
        break

    elif msg.startswith("send "):
        parts = msg.split(' ', 2)
        mbox_id, message = parts[1], parts[2]
        if mbox_id not in mailbox:
            mailbox[mbox_id] = []
        mailbox[mbox_id].append(message)
        s.sendto(b'OK', addr)

    elif msg.startswith("receive "):
        parts = msg.split(' ', 1)
        mbox_id = parts[1]
        if mbox_id in mailbox and mailbox[mbox_id]:
            response = mailbox[mbox_id].pop(0)
            s.sendto(response.encode(), addr)
        else:
            s.sendto(b'No messages', addr)

    else:
        s.sendto(b'Invalid command', addr)

s.close()
