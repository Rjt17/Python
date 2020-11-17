#!/usr/bin/env python

import socket

bind_ip = "127.0.0.1"
bind_port = 12345

server = socket.socket()
server.bind((bind_ip,bind_port))
print("socket is binded to %s" %(bind_port))
server.listen(100)

print("[*] Listening on {}:{}".format(bind_ip,bind_port))

while True:
	client, addr = server.accept()
	print("got connection from", addr)

	client.send("thankyou\n".encode())

	client.close()