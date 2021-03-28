import socket
import os
from _thread import *
from datetime import datetime
from pynput.keyboard import Key, Controller
import portforwardlib
import urllib.request
from pynput.keyboard import Key, Listener

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 5001
ThreadCount = 0
keyboard = Controller()

result = portforwardlib.forwardPort(port, port, None, host, "False", "TCP", 0, None, False)
print(result)
print(urllib.request.urlopen('https://ident.me').read().decode('utf8'))
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def set_keys():
    pressed = set()

    def on_press(key):
        if key == Key.esc:
            listener.stop()
            return
        if key not in pressed:
            pressed.add(str(key))
            print(key)

    with Listener(
            on_press=on_press) as listener:
        listener.join()
    return pressed

def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server'))
    allowed_keys = set_keys()
    allowedKeysMap = {
        "Key.right": Key.right,
        "Key.left": Key.left,
        "Key.up": Key.up,
        "Key.down": Key.down
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
        if len(reply[1]) == 1 or reply[1] in allowed_keys:
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
    start_new_thread(threaded_client, (Client,))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
