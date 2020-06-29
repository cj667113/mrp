import socket
import sys
import getopt
argumentList = sys.argv[1:] 
i=0
for element in argumentList:
	if element == "-i":
		MQTT_IP=argumentList[i+1]
	elif element == "-p":
		MQTT_PORT=argumentList[i+1]
	i=i+1
UDP_IP=""
UDP_PORT=5005
MESSAGE=b"%b,%b" %(bytes(MQTT_IP,'utf-8'),bytes(MQTT_PORT,'utf-8'))
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind((UDP_IP,UDP_PORT))
while True:
	data,addr = sock.recvfrom(1024)
	sock.sendto(MESSAGE,addr)
