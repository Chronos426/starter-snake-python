data = {"you": {"body": [{"y": 3, "x": 9}, {"y": 4, "x": 9}, {"y": 5, "x": 9}], "health": 94,
               "id": "gs_WdqV3GF3Vj6TDbjffScYMgG4", "shout": "", "name": "SnakeOne"}, "board": {
    "food": [{"y": 7, "x": 0}, {"y": 7, "x": 2}, {"y": 6, "x": 1}, {"y": 2, "x": 3}, {"y": 5, "x": 1}], "snakes": [
       {"body": [{"y": 3, "x": 9}, {"y": 4, "x": 9}, {"y": 5, "x": 9}], "health": 94,
         "id": "gs_WdqV3GF3Vj6TDbjffScYMgG4", "shout": "", "name": "SnakeOne"}], "width": 11, "height": 11},
    "turn": 6, "game": {"id": "08076fc9-07f0-462c-9ec7-59b3c8fdb08d"}}
chemin = [0, 0, 0, 0]

if data['board']['snakes'][0]['body'][0]['x'] is str:
    print("is none")

print(data['board']['snakes'][0]['body'][0]['x'])