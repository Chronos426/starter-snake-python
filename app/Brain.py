from  Nombre_passage_algo import nombre_case

#data = {u'game': {u'id': u'bf0cfccd-1e2f-474c-82a9-92f30ae64bf4'}, u'turn': 5, u'board': {u'width': 11, u'food': [{u'x': 10, u'y': 2}, {u'x': 2, u'y': 4}], u'height': 11, u'snakes': [{u'shout': u'', u'body': [{u'x': 1, u'y': 0}, {u'x': 1, u'y': 1}, {u'x': 1, u'y': 2}], u'name': u'SnakeOne', u'id': u'gs_xVWXycYGQShh3fWQVKk9gHRF', u'health': 95}, {u'shout': u'', u'body': [{u'x': 3, u'y': 6}, {u'x': 3, u'y': 7}, {u'x': 2, u'y': 7}], u'name': u'Random', u'id': u'gs_GStXcfJMJmDRxDhCTY8hYyJ9', u'health': 95}]}, u'you': {u'shout': u'', u'body': [{u'x': 1, u'y': 0}, {u'x': 1, u'y': 1}, {u'x': 1, u'y': 2}], u'name': u'SnakeOne', u'id': u'gs_xVWXycYGQShh3fWQVKk9gHRF', u'health': 95}}
#chemin = [0, 0, 0, 0]

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
        taille -= 2
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

    colision_tete(data, chemin)

    follow_tail(data, chemin)

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
    snake_id = []
    wich_snake = []

    for i in range(snake_number):

        if data['board']['snakes'][i]['id'] != data['you']['id']:

            wich_snake.append(i)
            snake_id.append(data['board']['snakes'][i]['id'])
            snake_position.append(data['board']['snakes'][i]['body'][0]['x'] - 1)
            snake_position.append(data['board']['snakes'][i]['body'][0]['y'])

            snake_position.append(data['board']['snakes'][i]['body'][0]['x'] + 1)
            snake_position.append(data['board']['snakes'][i]['body'][0]['y'])

            snake_position.append(data['board']['snakes'][i]['body'][0]['x'])
            snake_position.append(data['board']['snakes'][i]['body'][0]['y'] - 1)

            snake_position.append(data['board']['snakes'][i]['body'][0]['x'])
            snake_position.append(data['board']['snakes'][i]['body'][0]['y'] + 1)

    nombre_id = -1
    for i in range(0, len(snake_position), 2):

        if i%8 == 0:
            nombre_id += 1

        if head_x_1 - 1 == snake_position[i] and head_y_1 == snake_position[i+1]:
            if len(data['board']['snakes'][wich_snake[nombre_id]]['body']) >= len(data['you']['body']):
                chemin[0] -= 300
            else:
                chemin[0] += 10
        if head_x_1 + 1 == snake_position[i] and head_y_1 == snake_position[i+1]:
            if len(data['board']['snakes'][wich_snake[nombre_id]]['body']) >= len(data['you']['body']):
                chemin[1] -= 300
            else:
                chemin[1] += 10
        if head_x_1 == snake_position[i] and head_y_1 - 1 == snake_position[i+1]:
            if len(data['board']['snakes'][wich_snake[nombre_id]]['body']) >= len(data['you']['body']):
                chemin[2] -= 300
            else:
                chemin[2] += 10
        if head_x_1 == snake_position[i] and head_y_1 + 1 == snake_position[i+1]:
            if len(data['board']['snakes'][wich_snake[nombre_id]]['body']) >= len(data['you']['body']):
                chemin[3] -= 300
            else:
                chemin[3] += 10

def follow_tail(data, chemin):
    head_x_1 = data['you']['body'][0]['x']
    head_y_1 = data['you']['body'][0]['y']

    snake_length = len(data['you']['body'])
    if head_x_1 - 1 == data['you']['body'][snake_length - 1]['x'] and head_y_1 == data['you']['body'][snake_length - 1]['y']:
        chemin[0] += 1
    if head_x_1 + 1 == data['you']['body'][snake_length - 1]['x'] and head_y_1 == data['you']['body'][snake_length - 1]['y']:
        chemin[1] += 1
    if head_x_1 == data['you']['body'][snake_length - 1]['x'] and head_y_1 - 1 == data['you']['body'][snake_length - 1]['y']:
        chemin[2] += 1
    if head_x_1 == data['you']['body'][snake_length - 1]['x'] and head_y_1 + 1 == data['you']['body'][snake_length - 1]['y']:
        chemin[3] += 1

def food_path(data, chemin):
    head_x_1 = data['you']['body'][0]['x']
    head_y_1 = data['you']['body'][0]['y']

    nombre_food = len(data['board']['food'])
    distance_food = [100, 0, 0]

    for i in range(nombre_food):
        food_x = data['board']['food'][i]['x']
        food_y = data['board']['food'][i]['y']

        diff_x = head_x_1 - food_x
        diff_y = head_y_1 - food_y
        if abs(diff_y)+abs(diff_x) < distance_food[0]:
            distance_food[0] = abs(diff_x) + abs(diff_y)
            distance_food[1] = diff_x
            distance_food[2] = diff_y

    print("distance_food: " + str(distance_food[0]))
    print("diff_x: " + str(distance_food[1]))
    print("diff_y: " + str(distance_food[2]))

    if distance_food[1] != 0:
        if distance_food[1] > 0:
            chemin[0] += 2
        else:
            chemin[1] += 2

    if distance_food[2] != 0:
        if distance_food[2] > 0:
            chemin[2] += 2
        else:
            chemin[3] += 2

    return




