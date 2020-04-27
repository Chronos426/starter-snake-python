'''data = {"you": {"body": [{"y": 3, "x": 9}, {"y": 4, "x": 9}, {"y": 5, "x": 9}], "health": 94,
                "id": "gs_WdqV3GF3Vj6TDbjffScYMgG4", "shout": "", "name": "SnakeOne"}, "board": {
    "food": [{"y": 7, "x": 0}, {"y": 7, "x": 2}, {"y": 6, "x": 1}, {"y": 2, "x": 3}, {"y": 5, "x": 1}], "snakes": [
        {"body": [{"y": 3, "x": 9}, {"y": 4, "x": 9}, {"y": 5, "x": 9}], "health": 94,
         "id": "gs_WdqV3GF3Vj6TDbjffScYMgG4", "shout": "", "name": "SnakeOne"}], "width": 11, "height": 11},
        "turn": 6, "game": {"id": "08076fc9-07f0-462c-9ec7-59b3c8fdb08d"}}'''


def message(data):
    print(data)

def avoidwall(data):
    head_x_1 = data['you']['body'][0]['x']
    head_y_1 = data['you']['body'][0]['y']
    head_x_2 = data['you']['body'][1]['x']
    head_y_2 = data['you']['body'][1]['y']
    board_width = data['board']['width']
    board_height = data['board']['height']


    if head_x_1 > head_x_2:
        direction = 'E'
        front_tim = [head_x_1 + 1, head_y_1]
        left_tim = [head_x_1, head_y_1 - 1]
        right_tim = [head_x_1, head_y_1 + 1]
    elif head_x_1 < head_x_2:
        direction = 'O'
        front_tim = [head_x_1 - 1, head_y_1]
        left_tim = [head_x_1, head_y_1 + 1]
        right_tim = [head_x_1, head_y_1 - 1]
    elif head_y_1 < head_y_2:
        direction = 'N'
        front_tim = [head_x_1, head_y_1 - 1]
        left_tim = [head_x_1 - 1, head_y_1]
        right_tim = [head_x_1 + 1, head_y_1]
    else:
        direction = 'S'
        front_tim = [head_x_1, head_y_1 + 1]
        left_tim = [head_x_1 + 1, head_y_1]
        right_tim = [head_x_1 - 1, head_y_1]

    if head_x_1 == 0 and direction == 'O':
        if head_y_1 == 0:
            return 'down'
        else:
            return 'up'
    elif head_y_1 == 0 and direction == 'N':
        if head_x_1 == 0:
            return 'right'
        else:
            return 'left'
    elif head_y_1 == board_height - 1 and direction == 'S':
        if head_x_1 == 0:
            return 'right'
        else:
            return 'left'
    elif head_x_1 == board_width - 1 and direction == 'E':
        if head_y_1 == 0:
            return 'down'
        else:
            return 'up'
    else:
        if direction == 'E':
            return 'right'
        elif direction == 'O':
            return 'left'
        elif direction == 'N':
            return 'up'
        elif direction == 'S':
            return 'down'