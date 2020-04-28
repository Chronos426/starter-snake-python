'''data = {"you": {"body": [{"y": 3, "x": 9}, {"y": 4, "x": 9}, {"y": 5, "x": 9}], "health": 94,
                "id": "gs_WdqV3GF3Vj6TDbjffScYMgG4", "shout": "", "name": "SnakeOne"}, "board": {
    "food": [{"y": 7, "x": 0}, {"y": 7, "x": 2}, {"y": 6, "x": 1}, {"y": 2, "x": 3}, {"y": 5, "x": 1}], "snakes": [
        {"body": [{"y": 3, "x": 9}, {"y": 4, "x": 9}, {"y": 5, "x": 9}], "health": 94,
         "id": "gs_WdqV3GF3Vj6TDbjffScYMgG4", "shout": "", "name": "SnakeOne"}], "width": 11, "height": 11},
        "turn": 6, "game": {"id": "08076fc9-07f0-462c-9ec7-59b3c8fdb08d"}}'''


def message(data):
    print(data)

def choix_chemin(chemin):
    for i in range(4):
        if chemin[i] == max(chemin):
            return i

def body_detection(data,chemin):
    head_x_1 = data['you']['body'][0]['x']
    head_y_1 = data['you']['body'][0]['y']
    taille = len(data['you']['body'])
    taille -= 1
    for i in range(taille):
        if head_x_1 + 1 == data['you']['body'][i+1]['x'] and head_y_1 == data['you']['body'][i+1]['y']:
            chemin[1] -= 1000
        if head_x_1 - 1 == data['you']['body'][i+1]['x'] and head_y_1 == data['you']['body'][i+1]['y']:
            chemin[0] -= 1000
        if head_y_1 - 1 == data['you']['body'][i+1]['y'] and head_x_1 == data['you']['body'][i+1]['x']:
            chemin[2] -= 1000
        if head_y_1 + 1 == data['you']['body'][i+1]['y'] and head_x_1 == data['you']['body'][i+1]['x']:
            chemin[3] -= 1000
    return

def obstacle_detection(data):
    head_x_1 = data['you']['body'][0]['x']
    head_y_1 = data['you']['body'][0]['y']
    head_x_2 = data['you']['body'][1]['x']
    head_y_2 = data['you']['body'][1]['y']
    board_width = data['board']['width']
    board_height = data['board']['height']
    chemin = [0, 0, 0, 0]

    if head_x_1 == 0:
        chemin[0] -= 1000
    if head_x_1 == board_width - 1:
        chemin[1] -= 1000
    if head_y_1 == 0:
        chemin[2] -= 1000
    if head_y_1 == board_height - 1:
        chemin[3] -= 1000

    food_path(data, chemin)

    body_detection(data, chemin)

    direction = choix_chemin(chemin)
    print("chemin 0: " + str(chemin[0]))
    print("chemin 1: " + str(chemin[1]))
    print("chemin 2: " + str(chemin[2]))
    print("chemin 3: " + str(chemin[3]))
    print("direction: " + str(direction))

    if direction == 0:
        return 'left'
    elif direction == 1:
        return 'right'
    elif direction == 2:
        return 'up'
    elif direction == 3:
        return 'down'

def food_path(data, chemin):
    head_x_1 = data['you']['body'][0]['x']
    head_y_1 = data['you']['body'][0]['y']
    food_x = data['board']['food'][0]['x']
    food_y = data['board']['food'][0]['y']

    diff_x = head_x_1 - food_x
    diff_y = head_y_1 - food_y

    if abs(diff_x) >= abs(diff_y):
        if diff_x > 0:
            chemin[0] += 1
            return
        else:
            chemin[1] += 1
            return
    else:
        if diff_y > 0:
            chemin[2] += 1
            return
        else:
            chemin[3] += 1
            return