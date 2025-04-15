from socket import *
import os

# 웹 서버 포트는 80
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)
print('웹 서버가 시작되었습니다. 브라우저에서 http://127.0.0.1/index.html 입력')

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    request_line = req[0]
    tokens = request_line.split(' ')


    filename = tokens[1].lstrip('/')  # "/index.html" -> "index.html"


    # 파일이 존재하면 처리
    if os.path.exists(filename):
        # MIME 타입 결정
        if filename.endswith('.html'):
            mimeType = 'text/html'
            with open(filename, 'r', encoding='utf-8') as f:
                data = f.read()
            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: ' + mimeType + '\r\n'
            header += '\r\n'
            c.send(header.encode())
            c.send(data.encode('euc-kr'))  # 한글 깨짐 방지
        elif filename.endswith('.png'):
            mimeType = 'image/png'
            with open(filename, 'rb') as f:
                data = f.read()
            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: ' + mimeType + '\r\n'
            header += '\r\n'
            c.send(header.encode())
            c.send(data)
        elif filename.endswith('.ico'):
            mimeType = 'image/x-icon'
            with open(filename, 'rb') as f:
                data = f.read()
            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: ' + mimeType + '\r\n'
            header += '\r\n'
            c.send(header.encode())
            c.send(data)
        else:
            # 지원하지 않는 파일 형식
            response = 'HTTP/1.1 404 Not Found\r\n\r\n'
            response += '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
            response += '<BODY>Not Found</BODY></HTML>'
            c.send(response.encode('euc-kr'))
    else:
        # 파일 존재하지 않음
        response = 'HTTP/1.1 404 Not Found\r\n\r\n'
        response += '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
        response += '<BODY>Not Found</BODY></HTML>'
        c.send(response.encode('euc-kr'))

    c.close()
