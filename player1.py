

class Player:
  def __init__(self,position, opponentx, opponenty, sizex, sizey, max_obstacles):
    self.myx = position[1]
    self.myy = position[0]
    self.opponentx = opponentx
    self.opponenty = opponenty
    self.sizex = sizex
    self.sizey = sizey
    self.obstacles = []
    self.max_obstacles = max_obstacles
    self.my_goal_row = -1  # nomer finishnoy
    self.my_obstacles = 0 # kol-vo ustanovlennyh obstaclov
    #self.sir = [] # proydennye koordinaty



  def initialization(self, list_of_obstacles):
    self.obstacles = list_of_obstacles
    self.my_obstacles = 0 #ustanovlennyh prepyatstvii

    if (self.myy == 0):
      self.my_goal_row = self.sizey -1
  		#self.fixop = 0
    else:
      self.my_goal_row = 0
  		#self.fixop = size-1
    #print(self.my_goal_row)

  def move(self):
    if (self.myy != self.my_goal_row):
      if (self.my_goal_row == 0):
        #self.myy = self.myy - 1
        if (self.is_in_board(self.myx,self.myy - 1) and self.can_player_move(self.myx, self.myy - 1)):
          self.myy = self.myy - 1
        elif (self.is_in_board(self.myx + 1,self.myy) and self.can_player_move(self.myx + 1, self.myy)):
          self.myx = self.myx + 1
        elif (self.is_in_board(self.myx - 1,self.myy) and self.can_player_move(self.myx - 1, self.myy)):
          self.myx = self.myx - 1
        elif (self.is_in_board(self.myx,self.myy + 1) and self.can_player_move(self.myx,self.myy +1 )):
          self.myy = self.myy + 1
        else:
          pass
          #return [self.myy, self.myx]

      else:
        #self.myy = self.myy + 1
        if (self.is_in_board(self.myx,self.myy + 1) and self.can_player_move(self.myx, self.myy + 1)):
          self.myy = self.myy + 1
        elif (self.is_in_board(self.myx + 1,self.myy) and self.can_player_move(self.myx + 1, self.myy)):
          self.myx = self.myx + 1
        elif (self.is_in_board(self.myx - 1,self.myy) and self.can_player_move(self.myx - 1, self.myy)):
          self.myx = self.myx - 1
        elif (self.is_in_board(self.myx,self.myy - 1) and self.can_player_move(self.myx,self.myy - 1)):
          self.myy = self.myy - 1
        else:
          pass
          #return [self.myy, self.myx]

    #return [self.myy, self.myx]
  def update(self, position, opponentposition, barriers):
    self.myx = position[1]
    self.myy = position[0]
    self.opponentx = opponentposition[1]
    self.opponenty = opponentposition[0]
    self.obstacles = barriers

  def getter_position(self):
    return [self.myy, self.myx]

  def getter_opponentPosition(self):
    return [self.opponenty,self.opponentx]

  def getter_obstacles(self):
    return self.obstacles

  def getter_width(self):
    return self.sizex

  def getter_height(self):
    return self.sizey

  def is_in_board(self, x,y):
    if 0 <= x<self.sizex and 0 <= y <self.sizey:
      return True
    return False

  def can_player_move(self, newX,newY):
    if newX == self.opponentx and newY == self.opponenty:
        return False
    for row in self.obstacles:
      if (row[0][1] == row[1][1] and row[2][1] == row[3][1] and row[0][0] == row[2][0] and row[1][0] == row[3][0]):
        if ((self.myy == row[0][0] or self.myy == row[1][0]) and (self.myx == row[0][1] or self.myx == row[2][1])):
          if ((self.myy == row[0][0] and newY == row[1][0]) or (self.myy == row[1][0] and newY == row[0][0])):
            return False
      #vertical
      elif (row[0][0] == row[1][0] and row[2][0] == row[3][0] and row[0][1] == row[2][1] and row[1][1] == row[3][1]):
        if ((self.myx == row[0][1] or self.myx == row[1][0]) and self.myy == row[0][0] or self.myy == row[2][0]):
          if ((self.myx == row [1][1] and newX == row[0][1]) or (self.myx == row[0][1] and newX == row[1][1])):
            return False
      else:
        pass
    return True 