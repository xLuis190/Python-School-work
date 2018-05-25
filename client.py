from socketserver import *
import datetime

def modifyStr(s):
    if(len(s) == 0):
        return datetime.datetime.now()
    else:
        return None

class EchoHandler(BaseRequestHandler):
    def handle(self):
        bytes_message = self.requeset.recv(1024)
        str_message = bytes_message.decode()
        msgTosend = modityStr(str_message)
        self.request.send(msgToSend.encode())

echoServer = TCPServer(("172.26.2.204",1234),EchoHandler)

echoServer.serve_forever()
