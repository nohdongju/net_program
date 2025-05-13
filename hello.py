import argparse, socket, random
from datetime import datetime

BUFF_SIZE = 1024  # 수신 버퍼 크기 설정

def Server(ipaddr, port):
    """UDP 서버 함수"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP 소켓 생성
    sock.bind((ipaddr, port))  # IP와 포트에 바인딩
    print('Waiting in {}...'.format(sock.getsockname()))  # 서버 대기 출력

    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)  # 클라이언트로부터 데이터 수신
        if random.random() < prob:  # 확률적으로 패킷을 "손실"
            print('Message from {} is lost.'.format(addr))
            continue  # 응답하지 않고 다시 루프
        print('{} client message {!r}'.format(addr, data.decode()))  # 클라이언트 메시지 출력
        text = 'The length is {} bytes.'.format(len(data))  # 메시지 길이 정보 생성
        sock.sendto(text.encode(), addr)  # 클라이언트에게 응답 전송

def Client(hostname, port):
    """UDP 클라이언트 함수"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP 소켓 생성
    index = 1  # 메시지 번호
    time = 0.1  # 타임아웃 시간 설정 (초)

    while True:
        data = str(datetime.now())  # 현재 시간 문자열 생성
        sock.sendto(data.encode(), (hostname, port))  # 서버로 데이터 전송
        print('({}) Waiting for {} sec'.format(index, time))  # 타임아웃 시간 출력
        sock.settimeout(time)  # 타임아웃 설정

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)  # 서버로부터 응답 수신
        except socket.timeout:  # 타임아웃 발생 시
            time *= 2  # 타임아웃 시간 두 배 증가
            if time > 2.0:  # 최대 2초까지만 재시도
                print('{}th packet is lost'.format(index))
                if index >= sending_counts:  # 최대 횟수 도달 시 종료
                    break
                index += 1
                time = 0.1  # 타임아웃 초기화
            continue
        else:
            print('Server reply: {!r}'.format(data.decode()))  # 서버 응답 출력
            if index >= sending_counts:  # 메시지 전송 횟수 도달 시 종료
                break
            index += 1
            time = 0.1  # 타임아웃 초기화

if __name__ == '__main__':
    mode = {'c': Client, 's': Server}  # 역할에 따라 함수 선택
    parser = argparse.ArgumentParser(description='Send and receive UDP packets with setting drop probability')
    parser.add_argument('role', choices=mode, help='which role to take between server and client')  # 역할 선택
    parser.add_argument('-s', default='localhost', help='server that client sends to')  # 서버 주소
    parser.add_argument('-p', type=int, default=2500, help='UDP port (default:2500)')  # 포트 번호
    parser.add_argument('-prob', type=float, default=0, help='dropping probability (0~1)')  # 패킷 손실 확률
    parser.add_argument('-count', type=int, default=10, help='number of sending packets')  # 보낼 메시지 수
    args = parser.parse_args()

    prob = args.prob  # 전역 변수로 설정
    sending_counts = args.count

    if args.role == 'c':  # 클라이언트 실행
        mode[args.role](args.s, args.p)
    else:  # 서버 실행
        mode[args.role]('', args.p)
