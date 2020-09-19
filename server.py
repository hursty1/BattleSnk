import os
import random
from snk import Snk
import cherrypy

"""
This is a simple Battlesnake server written in Python.
For instructions see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""


class Battlesnake(object):
    # def __init__(self):
      
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        # This function is called when you register your Battlesnake on play.battlesnake.com
        # It controls your Battlesnake appearance and author permissions.
        # TIP: If you open your Battlesnake URL in browser you should see this data
        return {
            "apiversion": "1",
            "author": "not_a_snk",  # TODO: Your Battlesnake Username
            "color": "#4C89C8",  # TODO: Personalize
            "head": "silly",  # TODO: Personalize
            "tail": "curled",  # TODO: Personalize
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        # This function is called everytime your snake is entered into a game.
        # cherrypy.request.json contains information about the game that's about to be played.
        # TODO: Use this function to decide how your snake is going to look on the board.
        data = cherrypy.request.json
        self.snk = Snk(data["board"]["height"], data["board"]["width"])
        # self.snk.body = data["you"]["body"]
        # self.snk.head = data["you"]["head"]
        # self.snk.height = 
        # self.snk.width = 
        print(self.snk.board_size())
        print("START-------------------")
        print("START-------------------")
        print("START-------------------")
        return "ok"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        # TODO: Use the information in cherrypy.request.json to decide your next move.
        """
        game
        turn
        board
        you
        {
          'game': {'id': '1ff2fcf2-f7f3-4216-8a4e-bff82626a5be', 'ruleset': {'name': 'solo', 'version': 'v1.0.13'}, 'timeout': 500}, 
          'turn': 7, 
          'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_Gkp4Gw97cqMm9WwdjHWtqM4S', 'name': 'not_a_snk', 'latency': '62', 'health': 93, 'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}], 'head': {'x': 3, 'y': 8}, 'length': 3, 'shout': ''}], 'food': [{'x': 4, 'y': 10}, {'x': 5, 'y': 5}, {'x': 10, 'y': 2}, {'x': 7, 'y': 6}], 'hazards': []}, 
          'you': {'id': 'gs_Gkp4Gw97cqMm9WwdjHWtqM4S', 'name': 'not_a_snk', 'latency': '62', 'health': 93, 'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}], 'head': {'x': 3, 'y': 8}, 'length': 3, 'shout': ''}}
        """
        data = cherrypy.request.json
        
        self.snk.body = data["you"]["body"]
        self.snk.head = data["you"]["head"]
        # Choose a random direction to move in
        
        
        possible_moves = ["up", "down", "left", "right"]
        # move = random.choice(possible_moves)

        # print(f"MOVE: {}")
        return {"move": self.snk.move()}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # This function is called when a game your snake was in ends.
        # It's purely for informational purposes, you don't have to make any decisions here.
        data = cherrypy.request.json

        print("END")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)
