

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
        self.myy = self.myy - 1
      else:
        self.myy = self.myy + 1
    return [self.myy, self.myx]

  def setter_position(self, position, opponentposition, barriers):
    self.myx = position[1]
    self.myy = position[0]
    self.opponentx = opponentposition[1]
    self.opponenty = opponentposition[0]
    self.obstacles = barriers

  def getter_positon(self):
    return [self.myy, self.myx]

  def getter_opponentposition(self):
    return [self.opponenty,self.opponentx]

  def getter_obstacles(self):
    return [self.obstacles]

  def getter_width(self):
    return sizex

  def getter_height(self):
    return sizey

  def is_in_board(self, x,y):
    if 0 <= x<self.sizex and 0 <= y <self.sizey:
      return True
    return False

  def can_player_move(self, x,y):
    if x == self.opponentx and y == self.opponenty:
        return False
    for obstacle in self.obstacles:
        if not obstacle.can_player_move(self.myx, self.myy, x, y):
            return False
    if not self.is_in_board(x,y):
        return False
    if (abs(self.myy - y) == 1 and (self.myx == x)) or ((abs(self.myx - x)) == 1 and (self.myy == y)):
        return True
    else:
        return False
    return True
