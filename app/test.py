data = {"you": {"body": [{"y": 3, "x": 9}, {"y": 4, "x": 9}, {"y": 5, "x": 9}], "health": 94,
               "id": "gs_WdqV3GF3Vj6TDbjffScYMgG4", "shout": "", "name": "SnakeOne"}, "board": {
    "food": [{"y": 7, "x": 0}, {"y": 7, "x": 2}, {"y": 6, "x": 1}, {"y": 2, "x": 3}, {"y": 5, "x": 1}], "snakes": [
       {"body": [{"y": 3, "x": 9}, {"y": 4, "x": 9}, {"y": 5, "x": 9}], "health": 94,
         "id": "gs_WdqV3GF3Vj6TDbjffScYMgG4", "shout": "", "name": "SnakeOne"}], "width": 11, "height": 11},
    "turn": 6, "game": {"id": "08076fc9-07f0-462c-9ec7-59b3c8fdb08d"}}
chemin = [0, 0, 0, 0]


def nombre_case(data, chemin):
    board_width = data['board']['width']
    board_height = data['board']['height']
    head_x_1 = data['you']['body'][0]['x']
    head_y_1 = data['you']['body'][0]['y']
    chemin_passage = [0, 0, 0, 0]

    snake_number = len(data['board']['snakes'])

    board_matrice = []

    for i in range(board_height):
        board_matrice_ligne = []
        for j in range(board_width):
            board_matrice_ligne.append(0)
        board_matrice.append(board_matrice_ligne)

    for i in range(snake_number):
        snake_lenght = len(data['board']['snakes'][i]['body'])

        for j in range(snake_lenght):
            x = data['board']['snakes'][i]['body'][j]['x']
            y = data['board']['snakes'][i]['body'][j]['y']
            board_matrice[y][x] = 1

    board_passage = board_matrice
    passage = 0
    chemin_passage[0] = nombre_case_ia(head_x_1 - 1, head_y_1, board_passage, board_width, board_height, passage)

    print("chemin_passage_0")

    board_passage = board_matrice
    passage = 0
    chemin_passage[1] = nombre_case_ia(head_x_1 + 1, head_y_1, board_passage, board_width, board_height, passage)

    board_passage = board_matrice
    passage = 0
    chemin_passage[2] = nombre_case_ia(head_x_1, head_y_1 - 1, board_passage, board_width, board_height, passage)

    board_passage = board_matrice
    passage = 0
    chemin_passage[3] = nombre_case_ia(head_x_1, head_y_1 + 1, board_passage, board_width, board_height, passage)


    print(str(chemin_passage[0]))
    print(str(chemin_passage[1]))
    print(str(chemin_passage[2]))
    print(str(chemin_passage[3]))

def nombre_case_ia(x, y, board_passage, board_width, board_height, passage):

    if x >= 0 and y >= 0 and x < board_width and y < board_height:

        if board_passage[y][x] != 0:
            scan = False
            for i in range(board_height):
                if scan == True:
                    break
                print("i: " + str(i))
                for j in range(board_height):
                    print("j: " + str(j))
                    if i+1 < board_height - 1 and board_passage[i+1][j] == 0:
                        scan = True
                        break
                    if j+1 < board_width - 1 and board_passage[i][j+1] == 0:
                        scan = True
                        break
                    if i-1 >= 0 and board_passage[i][j+1] == 0:
                        scan = True
                        break
                    if j-1 >= 0 and board_passage[i][j+1] == 0:
                        scan = True
                        break
            if scan == False:
                return passage

        for i in range(board_height):
            for j in range(board_width):
                print(str(board_passage[i][j]), end='')
            print("")
        print("")

        if board_passage[y][x] != 1:
            if board_passage[y][x] == 0:
                passage += 1
                board_passage[y][x] = 2
                nombre_case_ia(x + 1, y, board_passage, board_width, board_height, passage)
                nombre_case_ia(x - 1, y, board_passage, board_width, board_height, passage)
                nombre_case_ia(x, y + 1, board_passage, board_width, board_height, passage)
                nombre_case_ia(x, y - 1, board_passage, board_width, board_height, passage)
            print(str(passage))


nombre_case(data,chemin)