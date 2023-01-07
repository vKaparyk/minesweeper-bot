from random import randint

from Board import Board


def place_bombs(board: Board, difficulty: tuple) -> None:
    bomb_list = []
    board_width, board_height = difficulty[0]
    
    # place random mines
    for i in range(difficulty[2]):
        while True:
            # TODO: check if current bomb count doesn't exceed max available space. will cause an infinite loop
            bomb = (randint(0, board_width - 1), randint(0, board_height - 1))
            if bomb not in bomb_list:
                bomb_list.append(bomb)
                break        
    for bomb in bomb_list:
        board.setBomb(bomb)
        
    # place numbers around bombs
    for x in range(board_width):
        for y in range(board_height):
            if board[x][y].isBomb:
                cells = board.get_list_near_coords((x, y))
                for cell in cells:
                    cell.bombNear()