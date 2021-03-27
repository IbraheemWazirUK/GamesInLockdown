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

pressed = {}

def on_press(key):
    if key not in pressed :
        pressed.add(key)
        r = "p {}".format(key)
        ClientSocket.send(r.encode())
        
def on_release(key):
    pressed.discard(key)
    r = "r {}".format(key)
    ClientSocket.send(r.encode())
   
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

