data = {"you": {"body": [{"y": 3, "x": 9}, {"y": 4, "x": 9}, {"y": 5, "x": 9}], "health": 94,
                "id": "gs_WdqV3GF3Vj6TDbjffScYMgG4", "shout": "", "name": "SnakeOne"}, "board": {
    "food": [{"y": 7, "x": 0}, {"y": 7, "x": 2}, {"y": 6, "x": 1}, {"y": 2, "x": 3}, {"y": 5, "x": 1}], "snakes": [
        {"body": [{"y": 3, "x": 9}, {"y": 4, "x": 9}, {"y": 5, "x": 9}], "health": 94,
         "id": "gs_WdqV3GF3Vj6TDbjffScYMgG4", "shout": "", "name": "SnakeOne"}], "width": 11, "height": 11},
        "turn": 6, "game": {"id": "08076fc9-07f0-462c-9ec7-59b3c8fdb08d"}}


def message(data):
    print(data)

def avoidwall(data):
    head_x = data['you']['body'][0]['x']
    head_y = data['you']['body'][0]['y']
    board_width = data['board']['width']
    board_height = data['board']['height']

    if head_x == 1:
        return 'down'
    if head_x == board_width-1:
        return 'up'
    if head_y == 1:
        return 'right'
    if head_y == board_height -1:
        return 'right'


message(data)
avoidwall(data)
