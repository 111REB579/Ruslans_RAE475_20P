#!/usr/bin/env python
#-*- coding: utf-8 -*-
import socket

HOST = ''                 #definē pieejamos interfeisus
PORT = 50007              #porta 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#definē socketa parametrus, piemēram: AF_net nozīme interneta domēnu
s.bind((HOST, PORT)) #norāda interfeisu un portu
print('Listening...') #ziņojuma izvade
s.listen(1) #socketa stavokļa parametrs
conn, addr = s.accept() #savienojuma akceptēšana
print('Connected by', addr) #ziņojuma izvade par lietotāju
while True: 
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data) #norāda parametrus par savienojumu
conn.close() #savienojuma izbeigšāna
