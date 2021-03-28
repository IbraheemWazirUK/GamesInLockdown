from threading import Thread
import ScreenServer2
import multiClientServer

def main():
    
    
    Thread(target = multiClientServer.main).start()
    Thread(target = ScreenServer2.main).start()

if __name__ == '__main__':
    main()`pyon3sc``dwa``
