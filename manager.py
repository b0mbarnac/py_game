from player1 import *

class Manager:
	def ___init___(self,p):
		self.p = p

	def first(self):
		self.p.move()
		tmpstr= "SOCKET STEP {{\"width\": {0}, \"height\": {1}, \"position\": {2}, \"opponentPosition\": {3}, \"barriers\": {4}}}".format(self.p.getter_width,self.p.getter_height,self.p.getter_position,self.p.getter_opponentPosition,self.p.getter_obstacles)
		return tmpstr

	def game(self,data):
		data = data[data.find("{"):]
		dictData = json.loads(data)
		self.p.update(dictData['position'],dictData['opponentPosition'],dictData[barriers])
		self.p.move()
		tmpstr= "SOCKET STEP {{\"width\": {0}, \"height\": {1}, \"position\": {2}, \"opponentPosition\": {3}, \"barriers\": {4}}}".format(self.p.getter_width,self.p.getter_height,self.p.getter_position,self.p.getter_opponentPosition,self.p.getter_obstacles)
		return tmpstr
