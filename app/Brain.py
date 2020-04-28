from  Nombre_passage_algo import nombre_case

#data = {"you": {"body": [{"y": 3, "x": 9}, {"y": 4, "x": 9}, {"y": 5, "x": 9}], "health": 94,
  #              "id": "gs_WdqV3GF3Vj6TDbjffScYMgG4", "shout": "", "name": "SnakeOne"}, "board": {
  #  "food": [{"y": 7, "x": 0}, {"y": 7, "x": 2}, {"y": 6, "x": 1}, {"y": 2, "x": 3}, {"y": 5, "x": 1}], "snakes": [
  #      {"body": [{"y": 3, "x": 9}, {"y": 4, "x": 9}, {"y": 5, "x": 9}], "health": 94,
  #       "id": "gs_WdqV3GF3Vj6TDbjffScYMgG4", "shout": "", "name": "SnakeOne"}], "width": 11, "height": 11},
  #  "turn": 6, "game": {"id": "08076fc9-07f0-462c-9ec7-59b3c8fdb08d"}}
#chemin = [0, 0, 0, 0]

def message(data):
    print(data)

def choix_chemin(chemin):
    for i in range(4):
        if chemin[i] == max(chemin):
            return i

def body_detection(data,chemin):
    head_x_1 = data['you']['body'][0]['x']
    head_y_1 = data['you']['body'][0]['y']

    nombre_snake = len(data['board']['snakes'])

    for j in range(nombre_snake):
        taille = len(data['board']['snakes'][j]['body'])
        taille -= 1
        for i in range(taille):
            if head_x_1 + 1 == data['board']['snakes'][j]['body'][i+1]['x'] and head_y_1 == data['board']['snakes'][j]['body'][i+1]['y']:
                chemin[1] -= 1000
            if head_x_1 - 1 == data['board']['snakes'][j]['body'][i+1]['x'] and head_y_1 == data['board']['snakes'][j]['body'][i+1]['y']:
                chemin[0] -= 1000
            if head_y_1 - 1 == data['board']['snakes'][j]['body'][i+1]['y'] and head_x_1 == data['board']['snakes'][j]['body'][i+1]['x']:
                chemin[2] -= 1000
            if head_y_1 + 1 == data['board']['snakes'][j]['body'][i+1]['y'] and head_x_1 == data['board']['snakes'][j]['body'][i+1]['x']:
                chemin[3] -= 1000
    return

def obstacle_detection(data):
    head_x_1 = data['you']['body'][0]['x']
    head_y_1 = data['you']['body'][0]['y']
    head_x_2 = data['you']['body'][1]['x']
    head_y_2 = data['you']['body'][1]['y']
    board_width = data['board']['width']
    board_height = data['board']['height']
    chemin = [0., 0., 0., 0.]

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

    nombre_case(data, chemin)

    colision_tete(data,chemin)

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


def colision_tete(data, chemin):
    head_x_1 = data['you']['body'][0]['x']
    head_y_1 = data['you']['body'][0]['y']
    snake_number = len(data['board']['snakes'])
    snake_position = []

    for i in range(snake_number):

       snake_position = snake_position.append(data['board']['snakes'][i]['body'][0]['x']) - 1
       snake_position = snake_position.append(data['board']['snakes'][i]['body'][0]['y'])

       snake_position = snake_position.append(data['board']['snakes'][i]['body'][0]['x']) + 1
       snake_position = snake_position.append(data['board']['snakes'][i]['body'][0]['y'])

       snake_position = snake_position.append(data['board']['snakes'][i]['body'][0]['x'])
       snake_position = snake_position.append(data['board']['snakes'][i]['body'][0]['y']) - 1

       snake_position = snake_position.append(data['board']['snakes'][i]['body'][0]['x'])
       snake_position = snake_position.append(data['board']['snakes'][i]['body'][0]['y']) + 1

    for i in snake_position:
        if head_x_1 - 1 == snake_position[i*2] and head_y_1 == snake_position[(i+1)*2]:
            chemin[0] -= 300
        if head_x_1 + 1 == snake_position[i*2] and head_y_1 == snake_position[(i+1)*2]:
            chemin[1] -= 300
        if head_x_1 == snake_position[i*2] and head_y_1 - 1 == snake_position[(i+1)*2]:
            chemin[2] -= 300
        if head_x_1 == snake_position[i*2] and head_y_1 + 1 == snake_position[(i+1)*2]:
            chemin[3] -= 300


def food_path(data, chemin):
    head_x_1 = data['you']['body'][0]['x']
    head_y_1 = data['you']['body'][0]['y']

    nombre_food = len(data['board']['food'])

    for i in range(nombre_food):
        food_x = data['board']['food'][i]['x']
        food_y = data['board']['food'][i]['y']

        diff_x = head_x_1 - food_x
        diff_y = head_y_1 - food_y

        if diff_x != 0:
            if diff_x > 0:
                chemin[0] += 1./diff_x
            else:
                chemin[1] += abs(1./diff_x)

        if diff_y != 0:
            if diff_y > 0:
                chemin[2] += 1./diff_y
            else:
                chemin[3] += abs(1./diff_y)
    return

