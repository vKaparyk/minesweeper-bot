from ExtraClass.Board import Board
from config import DIFFICULTY

from ImageProcessing import update_board

from MouseClicker import initialClick

from Algorithm import mainAlgorithm

def main():
    board = Board(DIFFICULTY[0], DIFFICULTY[2])

    initialClick()
    new_cells_counter = 0
    try:
        while True:
            new_cells = update_board(board)
            if not new_cells:
                new_cells_counter += 1
            else:
                new_cells_counter = 0
                
            if new_cells_counter > 2:
                break
            mainAlgorithm(board, new_cells)
    except KeyboardInterrupt:
        exit()
    print(board)


main()
