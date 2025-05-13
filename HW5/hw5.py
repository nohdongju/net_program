from socket import *       # 소켓 통신 모듈 import (TCP, UDP 등)
import os                  # 파일 경로 처리 모듈
import mimetypes           # 파일 확장자 → MIME 타입 매핑 모듈

# 서버 소켓 생성 및 바인딩 (포트 80은 HTTP 기본 포트)
s = socket()
s.bind(('', 80))           # 모든 IP에서 포트 80으로 수신
s.listen(10)               # 최대 대기 연결 수 10

# 현재 실행 중인 디렉토리 경로 저장 (파일 탐색용)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("서버 실행 중...")

while True:
    c, addr = s.accept()   # 클라이언트 접속 대기 → 연결 수락
    data = c.recv(1024)    # 클라이언트 요청 수신 (최대 1024바이트)
    msg = data.decode(errors='ignore')  # 디코딩 (깨짐 무시)
    req = msg.split('\r\n')             # 요청을 줄 단위로 분리
    request_line = req[0]               # 첫 줄이 요청 라인 (예: GET /index.html HTTP/1.1)
    print("요청:", request_line)

    try:
        # 요청 라인 파싱 (예: "GET /index.html HTTP/1.1")
        method, url, _ = request_line.split()

        # 요청한 파일 경로 구성 (예: /index.html → index.html)
        file_path = os.path.join(BASE_DIR, url.lstrip('/'))

        # 파일이 존재하고 GET 요청이면 처리
        if os.path.exists(file_path) and method == 'GET':
            # 파일의 MIME 타입을 추론
            mimeType, _ = mimetypes.guess_type(file_path)
            if mimeType is None:
                mimeType = 'application/octet-stream'  # 알 수 없으면 기본값

            # HTML 파일인 경우 (텍스트 응답)
            if mimeType == 'text/html':
                with open(file_path, 'r', encoding='utf-8') as f:
                    body = f.read()
                # 응답 헤더 전송 (200 OK)
                c.send(b'HTTP/1.1 200 OK\r\n')
                c.send(b'Content-Type: text/html; charset=euc-kr\r\n\r\n')
                # 응답 본문 전송 (euc-kr 인코딩으로 한글 깨짐 방지)
                c.send(body.encode('euc-kr'))

            # HTML이 아닌 이미지, 바이너리 파일 등
            else:
                with open(file_path, 'rb') as f:
                    body = f.read()
                header = f'HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n'
                c.send(header.encode())  # 헤더 전송
                c.send(body)             # 바이너리 파일 본문 전송

        # 파일이 없거나 GET이 아닌 경우 → 404 오류 응답
        else:
            not_found = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>' \
                         '<BODY>Not Found</BODY></HTML>'
            c.send(b'HTTP/1.1 404 Not Found\r\n')  # 상태 코드 전송
            c.send(b'\r\n')                        # 헤더 끝 표시
            c.send(not_found.encode('euc-kr'))     # 오류 페이지 본문 전송

    except:
        # 예외 발생 시 간단한 에러 응답
        c.send(b'Try again')

    c.close()  # 클라이언트 소켓 종료
