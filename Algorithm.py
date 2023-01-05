from random import randint

from config import EASY as board_difficulty
from config import BOARD as board

from helpers import print_board


def board_setup():
    board_width, board_height = board_difficulty[0]

    # init all values to 0
    for i in range(board_width):
        board.append([])
        for j in range(board_height):
            board[i].append(0)

    # place random mines
    bomb_list = []
    for i in range(board_difficulty[2]):
        while True:
            bomb = (randint(0, board_width - 1), randint(0, board_height - 1))
            if bomb not in bomb_list:
                bomb_list.append(bomb)
                break        
    for bomb in bomb_list:
        board[bomb[0]][bomb[1]] = "X"
        
    # place numbers around bombs
    for x in range(board_width):
        for y in range(board_height):
            if board[x][y] == "X":
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            if ((x + i) == board_width or (x + i) < 0) or ((y + j) == board_height or (y + j) < 0):
                                continue
                            try:
                                board[x + i][y + j] += 1
                            except TypeError:
                                pass

board_setup()


print_board(board)
