from socket import socket
from zlib import decompress
import cv2
import numpy
import pygame
from PIL import Image

WIDTH = 1000
HEIGHT = 800


def recvall(conn, length):
    """ Retreive all pixels. """

    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf


def main(host='127.0.0.1', port=5000):
    host = '0.0.0.0'
    watching = True

    sock = socket()
    sock.connect((host, port))
    try:
        width_len = int.from_bytes(sock.recv(1), byteorder='big')
        width = int.from_bytes(sock.recv(width_len), byteorder='big')
        height_len = int.from_bytes(sock.recv(1), byteorder='big')
        height = int.from_bytes(sock.recv(height_len), byteorder='big')

        while watching:

            # Retreive the size of the pixels length, the pixels length and pixels

            size_len = int.from_bytes(sock.recv(1), byteorder='big')
            size = int.from_bytes(sock.recv(size_len), byteorder='big')
            i = 0
            packet_size = 1024
            num_packets = size / packet_size

            pixels = []
            final_packet_size = size % packet_size
            while i < num_packets - 1:
                pixels.append(recvall(sock, packet_size))
                i += 1
            pixels.append(recvall(sock, final_packet_size))
            pixels = b"".join(pixels)

            #
            pixels = decompress(pixels)

            # Create the Surface from raw pixels
            img = Image.frombytes("RGB", (width, height), pixels)  # Convert to PIL.Image

            open_cv_image = numpy.array(img)
            open_cv_image = open_cv_image[:, :, ::-1].copy()
            cv2.imshow('image', open_cv_image)
            cv2.waitKey(1)
    finally:
        sock.close()


if __name__ == '__main__':
    main()
