#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket #izmantotā bibliotēka

msgFromClient       = "Hello UDP Server" #ziņojuma izvade
bytesToSend         = str.encode(msgFromClient) #baitu sakuma skaits
serverAddressPort   = ("127.0.0.1", 20001) #interfeisa parametri
bufferSize          = 1024 #bloku izmērs

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #socketa parametri
UDPClientSocket.sendto(bytesToSend, serverAddressPort) #nosūtīšanas parametri
msgFromServer = UDPClientSocket.recvfrom(bufferSize) #atbilde no servera
msg = "Message from Server {}".format(msgFromServer[0]) #ziņojums

print(msg) #ziņojuma izvade
