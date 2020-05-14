#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket #izmantotā bibliotēka

localIP     = "127.0.0.1" #interfeisa IP
localPort   = 20001 #ports
bufferSize  = 1024 #bloku izmērs

msgFromServer       = "Hello UDP Client" #ziņojuma izvade
bytesToSend         = str.encode(msgFromServer) #baitu sakuma skaits 

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #socketa parametri
UDPServerSocket.bind((localIP, localPort)) #IP piesaiste
print("UDP server up and listening") #ziņojuma izvade

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message) 
    clientIP  = "Client IP Address:{}".format(address) #parametru definešāna informācijas izvadei
    print(clientMsg) #ziņojuma izvade
    print(clientIP) #ziņojuma izvade
    UDPServerSocket.sendto(bytesToSend, address)
