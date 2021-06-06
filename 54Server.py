import socket
import sys
import json

def encrypt(message):
	obj = AES.new(b"aabbccddeeffgghh",AES.MODE_CFB,b"aabbccddeeffgghh")
	enc = obj.encrypt(message)
	return enc

def decrypt(message):
	obj = AES.new(b"aabbccddeeffgghh",AES.MODE_CFB,b"aabbccddeeffgghh")
	dec = obj.decrypt(message)
	return dec

s = socket.socket()
print ("Socket Created!")

port = 8008

s.bind(('', port))
print ("Socket binded to " + str(port))

s.listen(5)
print ("Socket is listening...")

file = open("test.txt", "wb")
print ("The file received named test.txt")

while True:
	c, addr = s.accept()
	print ("Got connection from " + str(addr))
	msg = ("Client [" + addr[0] + "] \nThank you, Come Again!")
	c.send(msg.encode())
	buffer = c.recv(1024)
	while buffer:
		file.write(buffer)
		buffer = c.recv(1024)
		file.close()
		print ("Successfully Received")
c.close() 
