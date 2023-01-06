from Board import Board
from config import DIFFICULTY
from helpers import place_bombs

board_width, board_height = DIFFICULTY[0]
board = Board(board_width, board_height)

def board_setup():
    place_bombs(board, DIFFICULTY)

board_setup()


print(board)
