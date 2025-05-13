from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        s = data.decode().strip()
        if '+' in s:
            a,b = s.split('+')
            result = str(int(a)+int(b))
        elif '-' in s:
            a,b = s.split('-')
            result = str(int(a)-int(b))
        elif '*' in s:
            a,b = s.split('*')
            result = str(int(a)*int(b))
        elif '/' in s:
            a,b = s.split('/')
            result = f'{int(a)/int(b):.1f}'
    
        client.send(result.encode())
        
client.close()

'''
from socket import *

# 서버 소켓 생성 (TCP)
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))          # 포트 3333에서 모든 IP 수신 허용
s.listen(5)                 # 최대 5개의 연결 대기
print('서버 대기 중...')

while True:
    client, addr = s.accept()      # 클라이언트 연결 수락
    print('클라이언트 접속:', addr)
    try:
        while True:
            data = client.recv(1024)   # 클라이언트 데이터 수신
            if not data:              # 연결 종료 시
                break

            s_input = data.decode().strip()  # 받은 문자열 정리
            try:
                # 사칙연산 처리
                if '+' in s_input:
                    a, b = map(int, s_input.split('+'))
                    result = str(a + b)
                elif '-' in s_input:
                    a, b = map(int, s_input.split('-'))
                    result = str(a - b)
                elif '*' in s_input:
                    a, b = map(int, s_input.split('*'))
                    result = str(a * b)
                elif '/' in s_input:
                    a, b = map(int, s_input.split('/'))
                    if b == 0:
                        result = '오류: 0으로 나눌 수 없습니다.'
                    else:
                        result = f'{a / b:.1f}'  # 소수 첫째 자리까지 표시
                else:
                    result = '오류: 지원하지 않는 연산입니다. (+, -, *, / 사용 가능)'

            except ValueError:
                result = '오류: 잘못된 입력 형식입니다. 예: 3+4'

            client.send(result.encode())  # 결과 전송

    except Exception as e:
        print(f"연결 중 오류 발생: {e}")

    client.close()
    print('클라이언트 연결 종료')
'''