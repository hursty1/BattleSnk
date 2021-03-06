import random
import math
import pandas as pd
import queue

class Snk:

	def __init__(self, height, width):
		self.height=height
		self.width=width
		self.food = []
		self.closets_food = ''
		self.body=[]
		self.head=[]
		self.next_move='left'
		self.possible_moves = ["left", "up", "right", "down"]

	def board_size(self):
		return [self.height, self.width]

	def snk_body(self):
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
		if self.head == self.closets_food: self.closets_food = {}
		self.find_closest_food()
		# moves = random_move(self.head, self.body, self.height)
		print(self.food)
		moves = move_to_food(self.head, self.body, self.height, self.closets_food)
		return str(moves)

	def find_closest_food(self):
		# print("Finding Closest food")
		if len(self.food) == 1: self.closets_food = self.food[0]
		if not self.closets_food:
			self.closets_food = self.food[0]
		dis = distance(self.head, self.closets_food)
		# if self.closets_food:
		# 	print("Closest food is: ", self.closets_food)
		for food in self.food:
			# print("Food is: ", food)
			if  distance(self.head, food) < dis:
				print("found new food")
				self.closets_food = food
				break

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
	# print("vectors are: ", v1, v2)
	return math.sqrt(math.pow(v1['x']-v2['x'], 2) + math.pow(v1['y']-v2['y'], 2))

def move_to_food(snk, body, size, food):
	"""
	Moves closer to food
	"""
	#snk = head
	#resolve x first
	if food:
		if snk['x'] != food['x']:
			if snk['x'] < food['x']:
				if valid(snk, body, size, ["right"]):
					return "right"
				else:
					return random_move(snk, body, size)
			else:
				#move to the left
				if valid(snk, body, size, ["left"]):
					return "left"
				else:
					return random_move(snk, body, size)
		
		if snk['y'] != food['y']:
			if snk['y'] < food['y']:
				#move to the down
				if valid(snk, body, size, ["up"]):
					return "up"
				else:
					return random_move(snk, body, size)
			else:
				#move to the up
				if valid(snk, body, size, ["down"]):
					return "down"
				else:
					return random_move(snk, body, size)
	else:
		return random_move(snk, body, size)