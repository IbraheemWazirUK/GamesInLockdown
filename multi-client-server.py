import socket
import os
from _thread import *
from datetime import datetime
from pynput.keyboard import Key, Controller

ServerSocket = socket.socket()
host = '192.168.1.250'
port = 5001
ThreadCount = 0
keyboard = Controller()

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server'))
    
    while True:
        data = connection.recv(2048)
        reply = data.decode('utf-8')
        validKeys = ['w', 'a', 's', 'd', 'g'] #Valid key presses
        if reply[3] in validKeys:
            print(f"Pressing {reply[3]}")
            if reply[0] == 'p':
                keyboard.press(reply[3])
            elif reply[0] == 'r':
                keyboard.release(reply[3])
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
