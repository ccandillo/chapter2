#!/usr/bin/env python

import argparse
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024

parser = argparse.ArgumentParser(description='Allow the user to specify a hostname and a port.')
parser.add_argument('--hostname', default=HOST, help='Add hostname')
parser.add_argument('--port', default=PORT, help='Add port')
args = parser.parse_args()

ADDR = (args.hostname, int(args.port))

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data.strip()
    tcpCliSock.close()

