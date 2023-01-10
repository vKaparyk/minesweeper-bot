from ExtraClass.Board import Board
from config import DIFFICULTY

from ImageProcessing import update_board

from MouseClicker import initialClick

from Algorithm import mainAlgorithm

def main():
    board = Board(DIFFICULTY[0], DIFFICULTY[2])

    initialClick()
    try:
        while True:
            new_cells = update_board(board)
            mainAlgorithm(board, new_cells)
    except KeyboardInterrupt:
        exit()
    print(board)


main()
