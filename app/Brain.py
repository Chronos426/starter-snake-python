def message(data):
    print(data)

def avoidwall(date):
    head_x = data['body'][0]['x']
    head_y = data['body'][0]['y']
    board_width = data['width']
    board_height = date['height']

    if head_x == 1:
       return 'down'
    if head_x == board_width-1:
        return 'up'
    if head_y == 1:
        return 'right'
    if head_y == board_height -1:
        return 'right'

