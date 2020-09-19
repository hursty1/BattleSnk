import random
import pandas as pd

class Snk:
    
  def __init__(self, height, width):
    self.height=height
    self.width=width
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
    x = int(self.head['x'])
    y = int(self.head['y'])
    n = self.check_boarders()
    if self.next_move == "left" and "left" not in n:
      self.next_move = "up"
    if self.next_move == "up" and "up" not in n:
      self.next_move = "right"
    if self.next_move == "right" and "right" not in n:
      self.next_move = "down"
    if self.next_move == "down" and "down" not in n:
      self.next_move = "left"
    #
    return str(self.next_move)
