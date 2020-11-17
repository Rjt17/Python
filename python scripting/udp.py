#!/usr/bin/env python

import socket

server_ip = "127.0.0.1"
server_port = 12345

messege = "hello, elitem!!".encode()

client = sockket.socket(socket.AF_INET, socket.DGRAM)

client.sendto(messege, (server_ip, server_port))