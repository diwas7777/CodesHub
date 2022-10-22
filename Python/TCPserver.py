'''
/ This is the server file
/ The client file is named as TCPclient.py
'''

from email import message
import socket

host = socket.gethostname()
port = 9337

sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_.bind((host,port))
sock_.listen(1)

print("\nServer Started.....\n")

conn, addr = sock_.accept()

print("Connected successfully to",str(addr))
message="\nThank you for connecting to the server"+str(addr)
conn.send(message.encode("ascii"))
conn.close()
