import socket
import sys
from _thread import *
import django
import os
from datetime import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("192.168.1.100", 5000))
print("server running ...")

"""
listens for 100 active connections. This number can be
increased as per convenience.
"""
server.listen(110)
LIST_OF_CLIENTS = []
CURRENT_TIME = 0

os.environ['DJANGO_SETTINGS_MODULE'] = 'interfaces.settings'
django.setup()
from ForcesApp.models import Colector_datos

def clientthread(conn, addr):
	global CURRENT_TIME

	while True:
			#try:
			message = conn.recv(4096).decode()
			if message:
				TC_Data, DESP_Data = message.split()
				now = datetime.now()
				TC_Data = float(TC_Data)
				fuerza =  TC_Data * 453.59 / 16.94		# calculo del peso a mandar a la base de datos
				print(now.strftime("%d/%m/%Y %H:%M:%S") + " " + message + " => " + str(fuerza))
				#print(f"{now} | {message} => {fuerza}")
				Colector_datos.objects.create(tiempo=int(DESP_Data), dato=int(fuerza), fecha=now.strftime("%d/%m/%Y %H:%M:%S"))
				CURRENT_TIME += 0.5


			else:
				print("error")
				remove(conn)

def remove(connection):
	if connection in LIST_OF_CLIENTS:
		LIST_OF_CLIENTS.remove(connection)

while True:

	"""Accepts a connection request and stores two parameters,
	conn which is a socket object for that user, and addr
	which contains the IP address of the client that just
	connected"""
	conn, addr = server.accept()

	"""Maintains a list of clients for ease of broadcasting
	a message to all available people in the chatroom"""
	LIST_OF_CLIENTS.append(conn)

	# prints the address of the user that just connected
	print (addr[0] + " connected")

	# creates and individual thread for every user
	# that connects
	start_new_thread(clientthread,(conn,addr))	

conn.close()
server.close()

