#!/usr/bin/env python

import socket

target_ip = "127.0.0.1"
target_port = 800

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("AAABBBCCC".encode(),(target_ip, target_port))

data, addr = client.recvfrom(1024)

print(data)