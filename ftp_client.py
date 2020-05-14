#!/usr/bin/env python
#-*- coding: utf-8 -*-
from ftplib import FTP #izmantotā bibliotēka

ftp = FTP('') #ftp savienojuma definēšāna
ftp.connect('localhost',1026) #kur pieslēgties
ftp.login() #logina pieprasišana
ftp.cwd('/home/russud/ftp')  #izmantotā mape
ftp.retrlines('LIST') #komanda kas parāda kas ir mapē

def uploadFile():
 filename = 'testfile.txt' #faila nosaukusm
 ftp.storbinary('STOR '+filename, open(filename, 'rb')) #norāda uz tipu kādā glabasies faili
 ftp.quit() #opcijas izbeikšana

def downloadFile():
 filename = 'testfile.txt' 
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024) #norāda uz tipu kādā lejuplādes faili
 ftp.quit() #opcijas izbeikšana
 localfile.close() #sesijas nobeigums

uploadFile()

