# -*- coding: utf-8 -*-

import os
import sys
import socket

reload(sys)
sys.setdefaultencoding('utf-8')

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 18080))
msg = ""
sendContent = 'GET /websocket HTTP/1.1\r\norigin:aa\r\nUpgrade:Websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Origin: http \r\n\r\n'
sk.send(sendContent);

RecvContent = sk.recv(1024)
print RecvContent

# stomp
sendContent = 'SEND\r\na:1\r\n{"a":1}'
sk.send(sendContent)
RecvContent = sk.recv(1024)
print RecvContent
