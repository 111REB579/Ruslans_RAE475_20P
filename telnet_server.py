#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import SocketServer #izmantotā bibliotēka
from telnetsrv.threaded import TelnetHandler, command #izmantotā bibliotēka

class MyHandler(TelnetHandler): #klases parametri un komandas

    WELCOME = "HI from Ruslan's server"
    @command('version')
    def version(self, params):
     self.writeresponse("V1.0")

class TelnetServer(SocketServer.TCPServer): #servera definēšāna
    allow_reuse_address = True
    

server = TelnetServer(("0.0.0.0", 10023), MyHandler) #servera definēšāna
server.serve_forever() #nozimē ka var atbildēt uz vairākiem pieprasijumiem
