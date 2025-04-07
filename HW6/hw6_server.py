from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
print("Server running...")

mboxes = {}

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    message = data.decode()
    tokens = message.split(maxsplit=2)

    if tokens[0] == "quit":
        print("Server shutting down.")
        break

    elif tokens[0] == "send" and len(tokens) >= 3:
        mboxId = tokens[1]
        msg_content = tokens[2]

        # 메시지를 저장
        if mboxId not in mboxes:
            mboxes[mboxId] = []
        mboxes[mboxId].append(msg_content)

        sock.sendto("OK".encode(), addr)
        print(f"[send] Stored '{msg_content}' to mailbox '{mboxId}'")

    elif tokens[0] == "receive" and len(tokens) >= 2:
        mboxId = tokens[1]

        # 메시지 존재 여부 확인 및 전송
        if mboxId in mboxes and mboxes[mboxId]:
            reply = mboxes[mboxId].pop(0)
            sock.sendto(reply.encode(), addr)
            print(f"[receive] Sent '{reply}' from mailbox '{mboxId}'")
        else:
            sock.sendto("No messages".encode(), addr)
            print(f"[receive] No messages in mailbox '{mboxId}'")

    else:
        sock.sendto("Invalid command".encode(), addr)
        print(f"[error] Invalid command received: {message}")

sock.close()
