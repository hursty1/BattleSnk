t = {
  "game": {
    "id": "game-00fe20da-94ad-11ea-bb37",
    "ruleset": {
      "name": "standard",
      "version": "v.1.2.3"
    },
    "timeout": 500
  },
  "turn": 14,
  "board": {
    "height": 11,
    "width": 11,
    "food": [
      {"x": 5, "y": 5}, 
      {"x": 9, "y": 0}, 
      {"x": 2, "y": 6}
    ],
    "hazards": [
      {"x": 3, "y": 2}
    ],
    "snakes": [
      {
        "id": "snake-508e96ac-94ad-11ea-bb37",
        "name": "My Snake",
        "health": 54,
        "body": [
          {"x": 0, "y": 0}, 
          {"x": 1, "y": 0}, 
          {"x": 2, "y": 0}
        ],
        "latency": "111",
        "head": {"x": 0, "y": 0},
        "length": 3,
        "shout": "why are we shouting??",
        "squad": ""
      }, 
      {
        "id": "snake-b67f4906-94ae-11ea-bb37",
        "name": "Another Snake",
        "health": 16,
        "body": [
          {"x": 5, "y": 4}, 
          {"x": 5, "y": 3}, 
          {"x": 6, "y": 3},
          {"x": 6, "y": 2}
        ],
        "latency": "222",
        "head": {"x": 5, "y": 4},
        "length": 4,
        "shout": "I'm not really sure...",
        "squad": ""
      }
    ]
  },
  "you": {
    "id": "snake-508e96ac-94ad-11ea-bb37",
    "name": "My Snake",
    "health": 54,
    "body": [
      {"x": 0, "y": 0}, 
      {"x": 1, "y": 0}, 
      {"x": 2, "y": 0}
    ],
    "latency": "111",
    "head": {"x": 0, "y": 0},
    "length": 3,
    "shout": "why are we shouting??",
    "squad": ""
  }
}
t2 = {'game': {'id': '47636a63-50ad-467a-8f66-e16d0d69f3d5', 'ruleset': {'name': 'solo', 'version': 'v1.0.17'}, 'timeout': 500}, 'turn': 229, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_fJdhRDcw7HxR4B43wrXKdxFW', 'name': 'not_a_snk', 'latency': '97', 'health': 74, 'body': [{'x': 6, 'y': 3}, {'x': 7, 'y': 3}, {'x': 7, 'y': 4}, {'x': 7, 'y': 5}, {'x': 7, 'y': 6}, {'x': 6, 'y': 6}, {'x': 6, 'y': 5}, {'x': 5, 'y': 5}, {'x': 5, 'y': 4}, {'x': 5, 'y': 3}, {'x': 4, 'y': 3}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}, {'x': 3, 'y': 3}], 'head': {'x': 6, 'y': 3}, 'length': 14, 'shout': ''}], 'food': [{'x': 6, 'y': 10}, {'x': 3, 'y': 10}, {'x': 2, 'y': 6}, {'x': 2, 'y': 9}, {'x': 4, 'y': 9}, {'x': 6, 'y': 9}, {'x': 2, 'y': 8}, {'x': 9, 'y': 7}, {'x': 0, 'y': 10}, {'x': 4, 'y': 10}, {'x': 7, 'y': 8}, {'x': 3, 'y': 9}, {'x': 4, 'y': 1}, {'x': 2, 'y': 3}, {'x': 1, 'y': 6}, {'x': 7, 'y': 1}, {'x': 9, 'y': 4}, {'x': 8, 'y': 1}, {'x': 5, 'y': 2}], 'hazards': []}, 'you': {'id': 'gs_fJdhRDcw7HxR4B43wrXKdxFW', 'name': 'not_a_snk', 'latency': '97', 'health': 74, 'body': [{'x': 6, 'y': 3}, {'x': 7, 'y': 3}, {'x': 7, 'y': 4}, {'x': 7, 'y': 5}, {'x': 7, 'y': 6}, {'x': 6, 'y': 6}, {'x': 6, 'y': 5}, {'x': 5, 'y': 5}, {'x': 5, 'y': 4}, {'x': 5, 'y': 3}, {'x': 4, 'y': 3}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}, {'x': 3, 'y': 3}], 'head': {'x': 6, 'y': 3}, 'length': 14, 'shout': ''}}
from snk_2 import Snk_2

s = Snk_2(11, 11)
s.store_data(t2)

print(s.board)
# print(s.valid_moves())
print(s.move())
