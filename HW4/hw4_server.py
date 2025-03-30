from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr =  s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break

        data = data.decode()
        try:
            if "+" in data:
                a, b = map(int, data.split("+"))
                result = str(a + b)
            elif "-" in data:
                a, b = map(int, data.split("-"))
                result = str(a - b)
            elif "*" in data:
                a, b = map(int, data.split("*"))
                result = str(a * b)
            elif "/" in data:
                a, b = map(int, data.split("/"))
                result = f"{a / b:.1f}"
            else:
                result = "try again"
        except Exception:
            result = "try again"

        client.send(result.encode())
    
    client.close()