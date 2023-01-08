from Board import Board
from config import DIFFICULTY
from helpers import place_bombs


def board_setup(board):
    place_bombs(board, DIFFICULTY)


# create dict: num -> list of func pointers, all taking current location and num (position will be determined in the func)
