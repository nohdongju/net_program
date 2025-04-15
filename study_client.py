import socket
import argparse

BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

parser = argparse.ArgumentParser()
parser.add_argument('-s', default='localhos')
parser.add_argument('-p', type=int,default=9999)
args = parser.parse_args()

s.connect((args.s, args.p))

while True:
    msg = input("Message to send: ")
    if msg == 'q':
        break
    s.send(msg.encode())
    data = s.recv(1024)
    if not data:
        break
    print('Received message: ', data.decode())
s.close()