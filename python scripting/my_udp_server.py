#!/usr/bin/env python

import socket

server_ip = "127.0.0.2"
server_port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((server_ip, server_port))

while True:
	print("[*] Listening on {}:{}".format(server_ip, server_port))
	data, addr = server.recvfrom(1024)
	print("messege: ", data)
	server.sendto("ACK!!!".encode(),(str(addr),800))

##errors