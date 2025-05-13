import socket
import threading
import time

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 2500))
s.listen(5)
print('Server Started')

def handle_client(client_socket, addr):

    client_id = client_socket.recv(1024).decode() 
    join_time = time.strftime('%a %b %d %H:%M:%S %Y')
    print(f"{join_time}{addr}:[{client_id}]")

    while True:
        try:
            message = client_socket.recv(1024)  
            if not message:
                break  

            if 'quit' in message.decode():  
                if client_socket in clients:
                    print(f'{client_id} ({addr}) exited')
                    clients.remove(client_socket)  
                break 

            send_time = time.strftime('%a %b %d %H:%M:%S %Y')
            print(f"{send_time}{addr}:{message.decode()}") 

            for client in clients:
                if client != client_socket: 
                    client.send(f"{message.decode()}".encode())

        except Exception as e:
            print(f"Error handling client {addr}: {e}")
            break

    print(f'Client {addr} ({client_id}) disconnected')
    if client_socket in clients: 
        clients.remove(client_socket)  
    client_socket.close() 

while True:
    client_socket, addr = s.accept() 
    print(f"New client connected: {addr}")

    clients.append(client_socket)  

    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.daemon = True
    client_thread.start()
