#!/usr/bin/env python

import socket
target_host = "127.0.0.1"
target_port = 12345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))

data = client.recv(1024)
print(data)
client.close()