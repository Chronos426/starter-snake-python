import copy
passage = 0

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
            if data['board']['snakes'][i]['body'][0]['x'] >= 0:
                board_matrice[data['board']['snakes'][i]['body'][0]['y']][data['board']['snakes'][i]['body'][0]['x'] - 1] = 1
            if data['board']['snakes'][i]['body'][0]['x'] <= board_width - 1:
                board_matrice[data['board']['snakes'][i]['body'][0]['y']][data['board']['snakes'][i]['body'][0]['x'] + 1] = 1
            if data['board']['snakes'][i]['body'][0]['y'] - 1 >= 0:
                board_matrice[data['board']['snakes'][i]['body'][0]['y'] - 1][data['board']['snakes'][i]['body'][0]['x']] = 1
            if data['board']['snakes'][i]['body'][0]['y'] + 1 <= board_width - 1:
                board_matrice[data['board']['snakes'][i]['body'][0]['y'] + 1][data['board']['snakes'][i]['body'][0]['x']] = 1

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
    passage = 0
    if x-1 >= 0 and board_passage[y][x-1] == 0:
        board_passage[y][x-1] = 2
        passage += 1
        construire_passage(x-1, y, board_passage, data)
    chemin_passage[0] = passage

    # right
    board_passage = copy.deepcopy(board_matrice)
    passage = 0
    if x+1 < board_width and board_passage[y][x+1] == 0:
        board_passage[y][x+1] = 2
        passage += 1
        construire_passage(x+1, y, board_passage, data)
    chemin_passage[1] = passage

    # up
    board_passage = copy.deepcopy(board_matrice)
    passage = 0
    if y-1 >= 0 and board_passage[y-1][x] == 0:
        board_passage[y-1][x] = 2
        passage += 1
        construire_passage(x, y-1, board_passage, data)
    chemin_passage[2] = passage

    # down
    board_passage = copy.deepcopy(board_matrice)
    passage = 0
    if y+1 < board_height and board_passage[y+1][x] ==0:
        board_passage[y+1][x] = 2
        passage += 1
        construire_passage(x, y+1, board_passage, data)
    chemin_passage[3] = passage

def construire_passage(x, y, board_passage, data):
    global passage
    board_width = data['board']['width']
    board_height = data['board']['height']

    # left
    if x-1 >= 0 and board_passage[y][x-1] == 0:
        board_passage[y][x-1] = 2
        passage += 1
        construire_passage(x-1, y, board_passage, data)

    # right
    if x+1 < board_width and board_passage[y][x+1] == 0:
        board_passage[y][x+1] = 2
        passage += 1
        construire_passage(x+1, y, board_passage, data)

    # up
    if y-1 >= 0 and board_passage[y-1][x] == 0:
        board_passage[y-1][x] = 2
        passage += 1
        construire_passage(x, y-1, board_passage, data)

    # down
    if y+1 < board_height and board_passage[y+1][x] ==0:
        board_passage[y+1][x] = 2
        passage += 1
        construire_passage(x, y+1, board_passage, data)

    return passage
