import socket
from threading import Thread
from zlib import compress
from mss import mss

# install mss



def retreive_screenshot(conn):
    with mss() as sct:
        # The region to capture
        monitor_1 = sct.monitors[1]
        img = sct.grab(monitor_1)
        width, height = img.size
        # send dimensions to client
        size_len = (width.bit_length() + 7) // 8
        conn.send(bytes([size_len]))
        size_bytes = width.to_bytes(size_len, 'big')
        conn.send(size_bytes)
        size_len = (height.bit_length() + 7) // 8
        conn.send(bytes([size_len]))
        size_bytes = height.to_bytes(size_len, 'big')
        conn.send(size_bytes)
        while 'recording':
            # Capture the screen
            monitor_1 = sct.monitors[1]
            img = sct.grab(monitor_1)
            print("img size dim : " + str(img.size))
            # Tweak the compression level here (0-9)
            # img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")  # Convert to PIL.Image
            # img.show()
            pixels = compress(img.rgb, 6)

            # Send the size of the pixels length
            size = len(pixels)
            size_len = (size.bit_length() + 7) // 8
            conn.send(bytes([size_len]))

            # Send the actual pixels length
            size_bytes = size.to_bytes(size_len, 'big')
            conn.send(size_bytes)
            # Send pixels
            packet_size = 1024
            final_packet_size = size % packet_size
            i = 0
            while i < (len(pixels) - packet_size):
                conn.send(pixels[i:i + packet_size])
                i += 1024

            conn.send(pixels[i:i + final_packet_size])
            # conn.sendall(pixels)


def main(host='', port=5002):
    host = socket.gethostbyname(socket.gethostname())
    sock = socket.socket()
    sock.bind((host, port))
    try:
        sock.listen(5)
        print('Server started.')

        while 'connected':
            conn, addr = sock.accept()
            print('Client connected IP:', addr)
            thread = Thread(target=retreive_screenshot, args=(conn,))
            thread.start()
    finally:
        sock.close()


if __name__ == '__main__':
    main()
