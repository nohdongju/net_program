import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024)  
            print(message.decode())  
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

svr_addr = ('localhost', 2500)  
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(svr_addr)  

my_id = input('ID를 입력하세요: ')  
sock.send(my_id.encode()) 

th = threading.Thread(target=receive_messages, args=(sock,))
th.daemon = True
th.start()

while True:
    msg = '[' + my_id + '] ' + input()  
    if msg.lower() == 'quit':
        sock.send(f'[{my_id}] is leaving the chat'.encode())  
        break
    sock.send(msg.encode()) 
