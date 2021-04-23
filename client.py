import socket
import string
import json
import re
import time
import player1 as p
import manager as m
import sys

sock = socket.socket()


sock.connect(('localhost', 5703))

data = "CONNECTION {{\"LOGIN\":\"{0}\"}}".format(sys.argv[1])
sock.send(data)
data = sock.recv(1024)
print(data)

data = "SOCKET JOINLOBBY {\"id\":null}"
sock.send(data)
data = sock.recv(2048)
print(data)


###parsing "JOINLOBBY"
dictData = json.loads(data)
id = dictData['DATA']['_id']
width = dictData['DATA']['width']
height = dictData['DATA']['height']
gameBarrierCount = dictData['DATA']['gameBarrierCount']
playerBarrierCount = dictData['DATA']['playerBarrierCount']
players_count = dictData['DATA']['players_count']


#sock.send("SOCKET STARTGAME")
data= sock.recv(2048)
print(data)

#parsing "STARTGAME"
data = data[data.find("{"):]
#print(data)
dictData = json.loads(data)
move = dictData['move']
position = dictData['position']
opponentPosition = dictData['opponentPosition']
barriers = dictData['barriers']

p1 = p.Player(position,opponentPosition[1],opponentPosition[0], width, height,playerBarrierCount)
p1.initialization(barriers)	
m1 = m.Manager(p1)

if (move == False):
	time.sleep(2)
	
else:
	tmpstr = m1.first()
	print(sys.argv[1])
	print('otpravil serveru')
	print(tmpstr)
	sock.send(tmpstr)
	time.sleep(2)
#playing
while True:

	data = sock.recv(2048)
	print(data)
	string = data
	if string[7:8] == 'E':
		break
	else:
		tmpstr= m1.game(string)
		print(sys.argv[1])
		print('otpravil serveru')
		print(tmpstr)
		sock.send(tmpstr)
	time.sleep(2)

sock.send("DISCONNECT {\"QUIT\":\"\"}")
data = sock.recv(2048)
print(data)
sock.close
