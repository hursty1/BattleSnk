import random
import numpy as np
import pandas as pd

class Snk_2:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.food = []
        self.closets_food = ''
        self.body = []
        self.head = []
        self.data = None
        self.game_id = ''
        self.possible_moves = ['left', 'up', 'right', 'down']
        self.next_move = self.possible_moves[random.randint(0, 3)]
    def board_size(self):
        # return [self.height, self.width]
        return np.zeros((self.height, self.width))

    def store_data(self, data):
        #1 = food, 2 = body, 3 = other snakes, 4 = hazards
        self.board = np.zeros((self.height, self.width))
        self.data = data
        for item in data['board']['snakes']:
            self.mapItem(item['body'], 3)
        # self.body = data['you']['body']
        self.head = data['you']['head']
        # self.food = data['board']['food']
        self.mapItem(data['board']['food'], 1)
        self.mapItem(data['you']['body'], 2)
        self.mapItem(data['you']['head'], 9)
        self.mapItem(data['board']['hazards'], 4)

    def mapItem(self, l, value):
        if type(l) is list and len(l) > 1:
            for item in l:
                Y = self.catesion(item['y'])
                X = item['x']
                self.board[Y][X] = value
        elif type(l) is list and len(l) == 1:
            Y = self.catesion(l[0]['y'])
            X = item['x']
            self.board[Y][X] =value
        elif type(l) is dict:
            Y = self.catesion(l['y'])
            X = l['x']
            self.board[Y][X] = value
            print("Saving Single")
        
    def valid_moves(self, X=None, Y=None):
        if X == None and Y == None:
            X, Y = self.head['x'], self.catesion(self.head['y'])
        valid = []
        if X + 1 < self.width:
            if self.board[Y][X+1] == 0 or self.board[Y][X+1] == 1:
                valid.append('right')
            else:
                print("Not Right")
        if X - 1 >= 0:
            if self.board[Y][X-1] == 0 or self.board[Y][X-1] == 1:
                valid.append('left')
            else:
                print("Not Left")
        if Y + 1 < self.height:
            if self.board[Y+1][X] == 0 or self.board[Y+1][X] == 1:
                valid.append('down')
            else:
                print("Not Up")
        if Y - 1 >= 0:
            if self.board[Y-1][X] == 0 or self.board[Y-1][X] == 1:
                valid.append('up')
            else:
                print("Not Down")
        self.validMoves = valid
        if len(valid) == 0: valid.append("up")
        return valid
    def catesion(self, y):
        "x value into battle snake x"
        return (self.height - 1) - y
    
    def calSize(self, move):
        X, Y = self.head['x'], self.catesion(self.head['y'])
        if move == 'right':
            X += 1
        if move == 'left':
            X -= 1
        if move == 'up':
            Y += 1
        if move == 'down':
            Y -= 1
        moves = self.valid_moves(X, Y)
        return len(moves)

    def longestPath(self, move):
        X, Y = self.head['x'], self.catesion(self.head['y'])
        count = 0
        if move == 'right':
            b = True
            X += 1
            while X < self.width and b:
                if (self.board[Y][X] in [0, 1]):
                    X += 1
                    count +=1
                else:
                    b = False
        if move == 'left':
            b = True
            X -= 1
            while X > 0 and b:
                if (self.board[Y][X] in [0, 1]):
                    X -= 1
                    count +=1
                else:
                    b = False
        if move == 'down':
            b = True
            Y += 1
            while Y < self.height and b:
                if (self.board[Y][X] in [0, 1]):
                    Y += 1
                    count += 1
                else:
                    b = False
        if move == 'up':
            b = True
            Y -= 1
            while Y > 0 and b:
                if (self.board[Y][X] in [0, 1]):
                    Y -= 1
                    count += 1
                else:
                    b = False
        return count

    def move(self):
        ##move the snake
        moves = self.valid_moves()
        strength=[]
        print("Move List is: ", moves)
        for move in moves:
            strength.append({move: self.longestPath(move)})

        df = pd.DataFrame(strength)
        se = df.max().sort_values(ascending=False)
        print("Longest move is: ", se)
        if len(se) > 2:
            se = se[:2]
            m = random.randint(0, abs(len(se) -1 ))
            if se[m] < 2:
                move = se.index[0]
            else:
                move = se.index[m]
        else:
            move = se.index[0]
        # move = moves[m]
        print('move is: ', move)
        return move

