from socket import *

port = 2500
BUFFSIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)

while True:
    time = 0
    msg = input('Enter a message: ')
    if msg == 'q':
        break   
    while True:
        sock.sendto(msg.encode(), ('localhost', port))
        print(f'Packet({time + 1}): Waiting up to {time + 1} sec for ack')
        sock.settimeout(1)
        try:
            data1, addr = sock.recvfrom(BUFFSIZE)
        except timeout:
            time += 1 
            if time > 3: 
                break
        else:
            if data1.decode() == 'ack':
                print('Response', data1.decode())
                data2, addr = sock.recvfrom(BUFFSIZE)
                print('Server says: ', data2.decode())
                break
sock.close()
