import SocketServer
from telnetsrv.threaded import TelnetHandler

class MyHandler(TelnetHandler):

    WELCOME = "HI from Ruslan's server"

class TelnetServer(SocketServer.TCPServer):
    allow_reuse_address = True

server = TelnetServer(("0.0.0.0", 10023), MyHandler)
server.serve_forever()
