import socket
import sys
import json

def encrypt(message):
	obj = AES.new(b"aabbccddeeffgghh",AES.MODE_CFB,b"aabbbccddeeffgghh")
	enc = obj.encrypt(message)
	return enc

def decrypt(message):
	obj = AES.new(b"aabbccddeeffgghh",AES.MODE_CFB,b"aabbccddeeffgghh")
	dec = obj.decrypt(message)
	return dec

s = socket.socket()

port = 8008

s.connect(('192.168.56.102', port))

print ("Select the File you want: ")
file = input("File Name: ")
print ("File name: " + file)

document = open(file, "rb")
DataTransf = document.read(1024)

while DataTransf:

	print ("The message received form the server are", s.recv(1024).decode("utf-8"))
	s.send(DataTransf)
	DataTransf = document.read(1024)

s.close()
