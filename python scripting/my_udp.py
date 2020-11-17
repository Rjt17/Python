#!/usr/bin/env python

import socket

server_ip = "127.0.0.2"
server_port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("{To end connection hit ENTER key at any stage...}")
while True:
	messege = input("type your messege to server: ")
	if messege == "":
		print("[*] Ending the conversation with the server...")
		break
	encoded_messege = messege.encode()

	client.sendto(encoded_messege, (server_ip, server_port))