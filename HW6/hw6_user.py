import socket
import time

device1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device1.connect(('localhost', 9001))

device2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device2.connect(('localhost', 9002))

f = open('data.txt', 'a')

while True:
    cmd = input("입력 > ")
    if cmd == '1':
        device1.send(b'Request')
        data = device1.recv(1024).decode()
        temp, humid, illum = data.split(',')
        timestamp = time.ctime()
        f.write(f'{timestamp}: Device1: Temp={temp}, Humid={humid}, Iilum={illum}\n')
        print("Device1 데이터 수신 및 저장 완료.")
    elif cmd == '2':
        device2.send(b'Request')
        data = device2.recv(1024).decode()
        heartbeat, steps, cal = data.split(',')
        timestamp = time.ctime()
        f.write(f'{timestamp}: Device2: Heartbeat={heartbeat}, Steps={steps}, Cal={cal}\n')
        print("Device2 데이터 수신 및 저장 완료.")
    elif cmd == 'quit':
        device1.send(b'quit')
        device2.send(b'quit')
        break
    else:
        print("try again")

f.close()
device1.close()
device2.close()
