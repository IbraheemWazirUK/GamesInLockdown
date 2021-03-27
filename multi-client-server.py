import socket
import os
from _thread import *
from datetime import datetime
from pynput.keyboard import Key, Controller
#import portforwardlib

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.250'
port = 5001
ThreadCount = 0
keyboard = Controller()

#result = portforwardlib.forwardPort(port, port, None, host, "False", "TCP", 0, None, False)

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server'))

    allowedKeysMap = {
        "Key.right": Key.right,
        "Key.left" : Key.left,
        "Key.up"   : Key.up,
        "Key.down" : Key.down
    }
    
    while True:
        data = connection.recv(2048)
        reply = data.decode('utf-8').split()
        print(f"received at {datetime.now().time()}")
        print(f"sent at {reply[2]}")
        print(f"Pressing {reply[1]}")
        print(f"Type {reply[0]}")
        print(f"Full reply {reply}")
        if reply[1][0] == "'":
            reply[1] = reply[1][1:-1]
        if len(reply[1]) == 1 or reply[1] in allowedKeysMap:
            if reply[0] == 'p':
                if reply[1] in allowedKeysMap:
                    keyboard.press(allowedKeysMap[reply[1]])
                else:
                    keyboard.press(reply[1])
            elif reply[0] == 'r':
                if reply[1] in allowedKeysMap:
                    keyboard.release(allowedKeysMap[reply[1]])
                else:
                    keyboard.release(reply[1])
        if not data:
            break
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
