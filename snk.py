import random
import math
import pandas as pd
import queue

class Snk:
    
  def __init__(self, height, width):
    self.height=height
    self.width=width
    self.food = []
    self.body=[]
    self.head=[]
    self.next_move='left'
    self.possible_moves = ["left", "up", "right", "down"]

  def board_size(self):
    return [self.height, self.width]

  def snk_body(self):
    #{'x': 3, 'y': 8}
    body = [self.head]
    body.append(body)
    return body

  def check_boarders(self):
    #checks boards to determine possible moves
    x = int(self.head['x'])
    y = int(self.head['y'])
    moves = ["left", "up", "right", "down"]
    # print(moves)
    if x - 1 < 0:
      moves.remove("left")
    if y + 1 >= self.height:
      moves.remove("up")
    if x + 1 >= self.width:
      moves.remove("right")
    if y - 1 < 0:
      moves.remove("down")
    return moves

  def move(self):
    print("finding Moves")
    moves = random_move(self.head, self.body, self.height)
    return str(moves)


def valid(snk, body, size, moves):
  """
  Determines if a move is out of bound or in body
  """
  # print("Snk is: ", snk)
  x = snk['x']
  y = snk['y']
  # print("Body is: ", body)
  b = []
  for item in body:
    
    b.append([item['x'], item['y']])

  for move in moves:
    if move == 'left':
      x -= 1
    elif move == 'right':
      x += 1
    elif move == 'up':
      y += 1
    elif move == 'down':
      y -= 1
    
    if not(0 <= x < size and 0 <= y < size):
      return False #out of bounds
    for item in b:
      if x == item[0] and y == item[1]:
        return False #body  
  return True


def random_move(snk, body, size):
    """
    Random but can't intentonally go off the board or onto itself 
    """
    possible_moves = ["left", "up", "right", "down"]
    move_next = True
    while move_next:
      move = random.choice(possible_moves)
      if valid(snk, body, size, [move]):
        move_next = False
      
    return move

def simple(snk, body, size, food):
  """
  Simple algorithm it should 
  """
  f = []
  for item in food:
    f.append([item['x'], item['y']])

  x, y = snk['x'], snk['y']
  f_len = []
  for i in f:
    d = math.sqrt(math.pow(x-i[0], 2) + math.pow(y-i[1], 2))
    f_len.append(d)
  closest = f_len.index(min(f_len))
  closest_food = food[closest]

  
