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

def distance(v1, v2):
  """
  Distance between two vectors
  """
  return math.sqrt(math.pow(v1[0]-v2[0], 2) + math.pow(v1[1]-v2[1], 2))


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


class Node():
  def __init__(self, parent=None, position=None):
    self.parent = parent
    self.position = position

    self.g = 0
    self.h = 0
    self.f = 0
  def __eq__(self, other):
    return self.position == other.position

def astar(board, start, end):
  """
  Returns a list of commands
  """
  start_node = Node(None, start)
  start_node.g = start_node.h = start_node.f = 0
  end_node = Node(None, end)

  #initalize both open and closed list
  open_list = []
  closed_list = []

  #add the start Node
  open_list.append(start_node)

  #loop until you find the end
  while len(open_list) > 0:
    current_node = open_list[0]
    current_index = 0
    for index, item in enumerate(open_list):
      if item.f < current_node.f:
        current_node = item
        current_index = index
    
    open_list.pop(current_index)
    closed_list.append(current_node)

    if current_node == end_node:
      path = []
      current = current_node
      while current is not None:
        path.append(current.position)
        current = current.parent
      return path[::-1] # Return reversed path
    
    children = []
    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: #adjcent squares
      node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
      
      if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)