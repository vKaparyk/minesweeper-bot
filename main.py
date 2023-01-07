from Board import Board
from config import DIFFICULTY

from ImageProcessing import update_board

def main():
    board = Board(DIFFICULTY[0])
    
    update_board(board)
    
    board.get_list_near_coords(5, 5)

main()