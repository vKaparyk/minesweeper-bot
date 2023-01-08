from Board import Board
from config import DIFFICULTY

from ImageProcessing import update_board


def main():
    board = Board(DIFFICULTY[0], DIFFICULTY[2])

    update_board(board)
    print(board)


main()
