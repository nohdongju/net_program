from socket import *
import os

s = socket()
s.bind(('', 80))
s.listen(10)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("서버 실행 중...")

while True:
    c, addr = s.accept()
    try:
        data = c.recv(1024)
        msg = data.decode(errors='ignore')
        req = msg.split('\r\n')
        request_line = req[0]
        print("요청:", request_line)

        method, url, _ = request_line.split()
        filename = url.lstrip('/')

        if method == 'GET' and url in ['/index.html', '/iot.png', '/favicon.ico']:
            file_path = os.path.join(BASE_DIR, filename)

            if os.path.exists(file_path):
                if filename == 'index.html':
                    mimeType = 'text/html'
                    with open(file_path, 'r', encoding='utf-8') as f:
                        body = f.read()
                    c.send(b'HTTP/1.1 200 OK\r\n')
                    c.send(f'Content-Type: {mimeType}\r\n\r\n'.encode())
                    c.send(body.encode('euc-kr'))

                elif filename == 'iot.png':
                    mimeType = 'image/png'
                    with open(file_path, 'rb') as f:
                        body = f.read()
                    c.send(b'HTTP/1.1 200 OK\r\n')
                    c.send(f'Content-Type: {mimeType}\r\n\r\n'.encode())
                    c.send(body)

                elif filename == 'favicon.ico':
                    mimeType = 'image/x-icon'
                    with open(file_path, 'rb') as f:
                        body = f.read()
                    c.send(b'HTTP/1.1 200 OK\r\n')
                    c.send(f'Content-Type: {mimeType}\r\n\r\n'.encode())
                    c.send(body)
            else:
                not_found = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>' \
                            '<BODY>Not Found</BODY></HTML>'
                c.send(b'HTTP/1.1 404 Not Found\r\n')
                c.send(b'\r\n')
                c.send(not_found.encode('euc-kr'))

        else:
            not_found = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>' \
                        '<BODY>Not Found</BODY></HTML>'
            c.send(b'HTTP/1.1 404 Not Found\r\n')
            c.send(b'\r\n')
            c.send(not_found.encode('euc-kr'))

    except Exception as e:
        print("에러:", e)
        c.send(b'HTTP/1.1 500 Internal Server Error\r\n\r\nTry again')

    c.close()
