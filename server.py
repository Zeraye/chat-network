import socket
from _thread import *
from user import User
import pickle
import json

with open('users.json', 'r+') as file:
    file.truncate()
    file.write('{}')

with open('database.txt', 'r+') as file:
    file.truncate()

# if you want it local
# server = socket.gethostbyname(socket.gethostname())
# if you want set up your own ip
server = ''
port = 7878

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen()
print('Waiting for connection, Server Started')

users = []


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


def write_json(data, filename='users.json'):
    with open(filename, 'r+') as file:
        json.dump(data, file, indent=4)


current_user = 0
while True:
    conn, addr = s.accept()
    print('Connected to:', addr)

    with open('users.json', 'r+') as file:
        print('im here')
        new_data = {str(current_user): ["", str(current_user), 'USER', []]}
        data = json.loads(file.read())
        data.update(new_data)
        write_json(data)
        print('appending...')
        users.append(User("", str(current_user), "", []))

    start_new_thread(threaded_client, (conn, current_user))
    current_user += 1

