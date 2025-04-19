import socket

LISTEN_PORT = 9000
DAUM_HOST = 'www.daum.net'
DAUM_PORT = 80
BUFFER = 4096

def handle_client(client_sock):
    # 1. 브라우저에서 요청 수신
    request = client_sock.recv(BUFFER).decode()
    print("Received from browser:\n", request)

    # 2. 요청 라인(GET ...)만 추출
    request_line = request.splitlines()[0]  # 첫 줄만 (예: GET / HTTP/1.1)

    # 3. 다음 서버에 요청 전송
    daum_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    daum_sock.connect((DAUM_HOST, DAUM_PORT))

    http_request = f"{request_line}\r\nHost: {DAUM_HOST}\r\n\r\n"
    daum_sock.sendall(http_request.encode())

    # 4. 다음 서버로부터 응답 수신
    while True:
        data = daum_sock.recv(BUFFER)
        if not data:
            break
        client_sock.sendall(data)  # 5. 브라우저에 전달

    # 6. 소켓 종료
    daum_sock.close()
    client_sock.close()

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('', LISTEN_PORT))
    server_sock.listen(1)
    print(f"Relay server listening on port {LISTEN_PORT}...")

    while True:
        client_sock, addr = server_sock.accept()
        print(f"Connected by {addr}")
        handle_client(client_sock)

if __name__ == '__main__':
    main()
