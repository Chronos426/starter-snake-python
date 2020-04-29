import copy
passage = 0

#data = {u'game': {u'id': u'bf0cfccd-1e2f-474c-82a9-92f30ae64bf4'}, u'turn': 5, u'board': {u'width': 11, u'food': [{u'x': 10, u'y': 2}, {u'x': 2, u'y': 4}], u'height': 11, u'snakes': [{u'shout': u'', u'body': [{u'x': 1, u'y': 0}, {u'x': 1, u'y': 1}, {u'x': 1, u'y': 2}], u'name': u'SnakeOne', u'id': u'gs_xVWXycYGQShh3fWQVKk9gHRF', u'health': 95}, {u'shout': u'', u'body': [{u'x': 3, u'y': 3}, {u'x': 3, u'y': 4}, {u'x': 2, u'y': 4}], u'name': u'Random', u'id': u'gs_GStXcfJMJmDRxDhCTY8hYyJ9', u'health': 95}]}, u'you': {u'shout': u'', u'body': [{u'x': 1, u'y': 0}, {u'x': 1, u'y': 1}, {u'x': 1, u'y': 2}], u'name': u'SnakeOne', u'id': u'gs_xVWXycYGQShh3fWQVKk9gHRF', u'health': 95}}
#chemin = [0, 0, 0, 0]

def nombre_case(data,chemin):
    head_x_1 = data['you']['body'][0]['x']
    head_y_1 = data['you']['body'][0]['y']
    board_width = data['board']['width']
    board_height = data['board']['height']
    chemin_passage = [0, 0, 0, 0]


    #matrice remplie de 0
    board_matrice = []
    for i in range(board_height):
        board_matrice_ligne = []
        for j in range(board_width):
            board_matrice_ligne.append(0)
        board_matrice.append(board_matrice_ligne)

    #matrice remplie de 0 et 1 en fct des snakes
    snake_number = len(data['board']['snakes'])
    for i in range(snake_number):
        snake_lenght = len(data['board']['snakes'][i]['body'])

        # Met la case atteignable par la tete d'un snake ennemy en 1
        if data['board']['snakes'][i]['id'] != data['you']['id']:
            if data['board']['snakes'][i]['body'][0]['x'] - 1 >= 0:
                board_matrice[data['board']['snakes'][i]['body'][0]['y']][data['board']['snakes'][i]['body'][0]['x'] - 1] = 3
            if data['board']['snakes'][i]['body'][0]['x'] < board_width - 1:
                board_matrice[data['board']['snakes'][i]['body'][0]['y']][data['board']['snakes'][i]['body'][0]['x'] + 1] = 3
            if data['board']['snakes'][i]['body'][0]['y'] - 1 >= 0:
                board_matrice[data['board']['snakes'][i]['body'][0]['y'] - 1][data['board']['snakes'][i]['body'][0]['x']] = 3
            if data['board']['snakes'][i]['body'][0]['y'] + 1 < board_width - 1:
                board_matrice[data['board']['snakes'][i]['body'][0]['y'] + 1][data['board']['snakes'][i]['body'][0]['x']] = 3

        for j in range(snake_lenght):
            x = data['board']['snakes'][i]['body'][j]['x']
            y = data['board']['snakes'][i]['body'][j]['y']
            board_matrice[y][x] = 1

    #calcule pour chaque direction le nombre de case atteignable
    calcul_passage(data, board_matrice, head_x_1, head_y_1, chemin_passage)

    print(str(chemin_passage))

    for i in range(4):
        chemin[i] += chemin_passage[i]


def calcul_passage(data, board_matrice, x, y, chemin_passage):
    global passage
    board_width = data['board']['width']
    board_height = data['board']['height']

    # left
    board_passage = copy.deepcopy(board_matrice)
    depth = 0
    passage = 0
    if x-1 >= 0 and board_passage[y][x-1] == 3:
        passage -= 2
        board_passage[y][x - 1] = 0
    if x-1 >= 0 and board_passage[y][x-1] == 0:
        board_passage[y][x-1] = 2
        passage += 1
        depth += 1
        construire_passage(x-1, y, board_passage, data, depth)
    chemin_passage[0] = passage

    # right
    board_passage = copy.deepcopy(board_matrice)
    depth = 0
    passage = 0
    if x+1 < board_width and board_passage[y][x+1] == 3:
        passage -= 2
        board_passage[y][x + 1] = 0
    if x+1 < board_width and board_passage[y][x+1] == 0:
        board_passage[y][x+1] = 2
        passage += 1
        depth += 1
        construire_passage(x+1, y, board_passage, data, depth)
    chemin_passage[1] = passage

    # up
    board_passage = copy.deepcopy(board_matrice)
    depth = 0
    passage = 0
    if y-1 >= 0 and board_passage[y - 1][x] == 3:
        passage -= 2
        board_passage[y-1][x] = 0
    if y-1 >= 0 and board_passage[y-1][x] == 0:
        board_passage[y-1][x] = 2
        passage += 1
        depth += 1
        construire_passage(x, y-1, board_passage, data, depth)
    chemin_passage[2] = passage

    # down
    board_passage = copy.deepcopy(board_matrice)
    depth = 0
    passage = 0
    if y+1 < board_height and board_passage[y + 1][x] == 3:
        passage -= 2
        board_passage[y+1][x] = 0
    if y+1 < board_height and board_passage[y+1][x] ==0:
        board_passage[y+1][x] = 2
        passage += 1
        depth += 1
        construire_passage(x, y+1, board_passage, data, depth)
    chemin_passage[3] = passage

def construire_passage(x, y, board_passage, data, depth):
    global passage
    board_width = data['board']['width']
    board_height = data['board']['height']

    print(str(depth))

    if depth >= 6:
        return passage

    # left
    if x-1 >= 0 and board_passage[y][x-1] == 3:
        passage -= 2
        board_passage[y][x - 1] = 0
    if x-1 >= 0 and board_passage[y][x-1] == 0:
        board_passage[y][x-1] = 2
        passage += 1
        depth += 1
        construire_passage(x-1, y, board_passage, data, depth)

    # right
    if x+1 < board_width and board_passage[y][x+1] == 3:
        passage -= 2
        board_passage[y][x + 1] = 0
    if x+1 < board_width and board_passage[y][x+1] == 0:
        board_passage[y][x+1] = 2
        passage += 1
        depth += 1
        construire_passage(x+1, y, board_passage, data, depth)

    # up
    if y-1 >= 0 and board_passage[y - 1][x] == 3:
        passage -= 2
        board_passage[y-1][x] = 0
    if y-1 >= 0 and board_passage[y-1][x] == 0:
        board_passage[y-1][x] = 2
        passage += 1
        depth += 1
        construire_passage(x, y-1, board_passage, data, depth)

    # down
    if y+1 < board_height and board_passage[y + 1][x] == 3:
        passage -= 2
        board_passage[y+1][x] = 0
    if y+1 < board_height and board_passage[y+1][x] == 0:
        board_passage[y+1][x] = 2
        passage += 1
        depth += 1
        construire_passage(x, y+1, board_passage, data, depth)

    return passage
