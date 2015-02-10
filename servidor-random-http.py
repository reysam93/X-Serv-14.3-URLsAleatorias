#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 9999))
mySocket.listen(3)

try:
    while True:
        print "Waiting for connections"
        (recvSocket, addr) = mySocket.accept()
        newURL = random.randint(0, 1000)
        print "request received: " + recvSocket.recv(2048)
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><p><a href=" + str(newURL) +
                        ">Dame otra''" +
                        "</a></p></body></html>\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
