from socket import *
import os
import mimetypes

s = socket()
s.bind(('', 80)) 
s.listen(10)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("서버 실행 중...")

while True:
    c, addr = s.accept()
    
    data = c.recv(1024)
    msg = data.decode(errors='ignore')
    req = msg.split('\r\n')
    request_line = req[0]
    print("요청:", request_line)

    try:
        method, url, _ = request_line.split()

        file_path = os.path.join(BASE_DIR, url.lstrip('/'))

        if os.path.exists(file_path) and method == 'GET':
            mimeType, _ = mimetypes.guess_type(file_path)
            if mimeType is None:
                mimeType = 'application/octet-stream'

            if mimeType == 'text/html':
                with open(file_path, 'r', encoding='utf-8') as f:
                    body = f.read()
                c.send(b'HTTP/1.1 200 OK\r\n')
                c.send(b'Content-Type: text/html; charset=euc-kr\r\n\r\n')
                c.send(body.encode('euc-kr'))
            else:
                with open(file_path, 'rb') as f:
                    body = f.read()
                header = f'HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n'
                c.send(header.encode())
                c.send(body)

        else:
            not_found = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>' \
                        '<BODY>Not Found</BODY></HTML>'
            c.send(b'HTTP/1.1 404 Not Found\r\n')
            c.send(b'\r\n')
            c.send(not_found.encode('euc-kr'))

    except:
        c.send(b'Try again')


    c.close()
