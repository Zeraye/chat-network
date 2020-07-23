import socket
from _thread import *
from user import User
import pickle

server = '192.168.8.116'
# server = socket.gethostname()
port = 9090

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print('Waiting for connection, Server Started')

conv = []
users = [User('Jakub', 'ADMIN', conv), User('Adam', 'USER', conv)]


def threaded_client(conn, user):
    conn.send(pickle.dumps(users[user]))
    reply = ''
    while True:
        try:
            data = pickle.loads(conn.recv(2048*4))
            users[user] = data

            if not data:
                print('Disconnect')
                break
            else:
                if user == 1:
                    reply = users[0]
                else:
                    reply = users[1]
                print('Received: ', data)
                print('Sending: ', reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print('Lost connection')
    conn.close()


current_user = 0
while True:
    conn, addr = s.accept()
    print('Connected to:', addr)

    start_new_thread(threaded_client, (conn, current_user))
    current_user += 1

