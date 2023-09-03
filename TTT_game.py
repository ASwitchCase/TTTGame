import random

class tick_ai:
  def __init__(self):
    self.win_condition = [
    [(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],
    [(2,0),(2,1),(2,2)],[(0,0),(1,0),(2,0)],
    [(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],
    [(2,0),(1,1),(0,2)],[(0,0),(1,1),(2,2)]]
    self.strat = random.randint(0,len(self.win_condition) - 1)
  

  def valid_strat(self,game):
    #print("strat# = " + str(self.strat) + " length = " + str(len(self.win_condition)))

    if self.strat != len(self.win_condition):
      for cord in self.win_condition[self.strat]:
        if game.grid[cord[0]][cord[1]] == "X":
          self.win_condition.pop(self.strat)
          return False
    return True
  
  def CPU_select(self,game):
    stop = False
    while not self.valid_strat(game) and stop == False:
      if len(self.win_condition) > 1:
        self.strat = random.randint(0,len(self.win_condition)- 1)
      else:
        stop = True

    if len(self.win_condition) > 1:    
      game.enter_play(self.win_condition[self.strat][0][0] + 1,self.win_condition[self.strat][0][1] + 1,"O")
      self.win_condition[self.strat].pop(0)
    else:
      sel = (random.randint(1, 3),random.randint(1, 3))
      while not game.is_open(sel[0],sel[1]):
        sel = (random.randint(1, 3),random.randint(1, 3))   
      game.enter_play(sel[0],sel[1],"O")

class TTTGame:
  def __init__(self):
    self.grid = [
      ["_","_","_"],
      ["_","_","_"],
      ["_","_","_"]]

  def show_grid(self):
    for x in self.grid: 
      print("")
      print("             "+ x[0] + " | " + x[1] + " | " + x[2])

    print("")
    print("*******************************************")
  
  def enter_play(self,x,y,play): #if 0 then enter again
    if self.grid[x -1][y -1] == "_":
      self.grid[x-1][y-1] = play
    else:
      return 0

  def full(self):
    for x in self.grid:
      for y in x:
        if y == "_":
          return False
    return True

  def is_open(self,x,y):
    if self.grid[x -1][y -1] == "_":
      return True
    return False

  def gameover(self):
    if self.grid[0][0] == self.grid[0][1] == self.grid[0][2] != "_":
      return True
    elif self.grid[1][0] == self.grid[1][1] == self.grid[1][2] != "_":
      return True
    elif self.grid[2][0] == self.grid[2][1] == self.grid[2][2] != "_":
      return True

    elif self.grid[0][0] == self.grid[1][0] == self.grid[2][0] != "_":
      return True
    elif self.grid[0][1] == self.grid[1][1] == self.grid[2][1] != "_":
      return True
    elif self.grid[0][2] == self.grid[1][2] == self.grid[2][2] != "_":
      return True
    
    elif self.grid[2][0] == self.grid[1][1] == self.grid[0][2] != "_":
      return True
    elif self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != "_":
      return True
    else:
      return False


#last person who played wins

b = TTTGame()
c = tick_ai()
lastplay = "X"



while not b.gameover() and not b.full():
  x = 0
  y = 0
  b.show_grid()
  print("Enter your play.")
  x = int(input("Row: "))
  y = int(input("Col: "))

  while not b.is_open(x,y):
    print("Spot taken, enter again.")
    x = int(input("Row: "))
    y = int(input("Col: "))
  
  b.enter_play(x,y,"X")

  if not b.gameover() and b.full():
    lastplay = "None"
  else:
    lastplay = "X"

  if not b.gameover() and not b.full():
    print("The Computer made a play")
    c.CPU_select(b)
    lastplay = "O"

if lastplay == "X":
  print("Three in a row, you win!")
elif lastplay == "O":
  print("Game Over, computer wins.")
else:
  print("Game Over draw.")

b.show_grid()
