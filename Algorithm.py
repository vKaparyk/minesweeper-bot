from Board import Board
from config import DIFFICULTY
from helpers import place_bombs

def board_setup(board):
    place_bombs(board, DIFFICULTY)