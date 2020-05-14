#!/usr/bin/env python
#-*- coding: utf-8 -*-
from pyftpdlib.authorizers import DummyAuthorizer #izmantotā bibliotēka
from pyftpdlib.handlers import FTPHandler #izmantotā bibliotēka
from pyftpdlib.servers import FTPServer #izmantotā bibliotēka

authorizer = DummyAuthorizer() #norāda klasi lietotājiem
authorizer.add_user("rus_sud", "12345", "/home/russud/ftp", perm="elradfmw") #definē lietotāju
authorizer.add_anonymous("/home/russud", perm="elradfmw") #nenoteikts lietotājs

handler = FTPHandler #norāda autorizācijas veidu
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler) #definē serveri
server.serve_forever() #nozimē ka var atbildēt uz vairākiem pieprasijumiem
