# -*- coding: utf-8 -*-
import SocketServer
from telnetsrv.threaded import TelnetHandler, command

class MyHandler(TelnetHandler):

    WELCOME = "HI from Ruslan's server"

class TelnetServer(SocketServer.TCPServer):
    allow_reuse_address = True

class MyHandler(TelnetHandler):
    @command('version')
    def version(self, params):
        self.writeresponse("V1.0")

server = TelnetServer(("0.0.0.0", 10023), MyHandler)
server.serve_forever()
