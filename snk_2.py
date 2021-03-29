import random
import numpy as np

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
                X = self.catesion(item['x'])
                self.board[X][ item['y'] ] = value
        elif type(l) is list and len(l) == 1:
            X = self.catesion(l[0]['x'])
            self.board[X][l[0]['y']] =value
        elif type(l) is dict:
            X = self.catesion(l['x'])
            self.board[X][l['y']] = value
            print("Saving Single")
        
    def valid_moves(self):
        X, Y = self.head['x'], self.head['y']
        valid = []
        if self.board[X+1][Y] == 0 or self.board[X+1][Y] == 1:
            valid.append('right')
        elif self.board[X-1][Y] == 0 or self.board[X-1][Y] == 1:
            valid.append('left')
        elif self.board[X][Y+1] == 0 or self.board[X][Y+1] == 1:
            valid.append('up')
        elif self.board[X][Y-1] == 0 or self.board[X][Y-1] == 1:
            valid.append('down')
        self.validMoves = valid
        return valid
    def catesion(self, x):
        "x value into battle snake x"
        return (self.height - 1) - x
    def move(self):
        ##move the snake
        moves = self.valid_moves()
        m = random.randint(0, (1 - len(moves)))
        move = moves[m]
        # print('move is: ', move)
        return move

