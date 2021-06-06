import socket
import sys
import json

mydata = {"id": 865666, "name": "Aidil", "age": "22"}
sendData = json.dumps(mydata)

s = socket.socket()
print("Socket successfully created")

port = 8877

s.connect(('192.168.56.102', port))

data = s.recv(1024)
data = data.decode("utf-8")

s.send(b'Thank you from client!')

dataJ = json.loads(data)

print(type(dataJ))
print(dataJ)

s.close()

