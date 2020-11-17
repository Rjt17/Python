import socket

target_host = "0.0.0.0"
target_port = 9991

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))

byt = "RAJAT".encode()

client.send(byt)

response = client.recv(4096).decode()

print(response)
