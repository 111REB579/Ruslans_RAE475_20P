#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import socket #izmantotā bibliotēka

HOST = '127.0.0.1'  #attālinātais serveris	
PORT = 50007          #ports    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #definē socketa parametrus, piemēram: AF_net nozīme interneta domēnu
print('Connecting...') #ziņojuma izvade
s.connect((HOST, PORT)) #socketa pieslekšanas paramets
s.sendall(b'Hello, world') #datu izvade
data = s.recv(1024) #datu bloka izmērs (MTU)
s.close() #socketa noslēģšana
print('Received', repr(data)) #paziņojums par dati parraidi 
