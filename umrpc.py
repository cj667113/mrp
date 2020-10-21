import socket
UDP_IP="255.255.255.255"
UDP_PORT=5005
MESSAGE=b"MQTT Resolution"
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(MESSAGE,(UDP_IP,UDP_PORT))
data,addr = sock.recvfrom(1024)
print(data)
