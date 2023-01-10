from ExtraClass.Board import Board
from ExtraClass.NearbyCells import NearbyCells

from config import DIFFICULTY
from helpers import place_bombs

from MouseClicker import rclickCell, clickCell, mclickCell


def mainAlgorithm(board: Board, new_cells: list):
    if not new_cells:
        new_cells = board.getAllLocalNumbers()
        # TODO: stop infinite loop

    for loc in new_cells:
        checkForImmediate(board, loc)


def checkForImmediate(board: Board, location: tuple):
    current_cell = board.get(location)
    nearby_cells = NearbyCells(board, location)
    
    
    if (current_cell.count) == (len(nearby_cells.unknown_cells_pos) + len(nearby_cells.bombs)):
        for i in nearby_cells.unknown_cells_pos:
            setBomb(board, i)
    nearby_cells.update()
    if current_cell.count == len(nearby_cells.bombs):
        mclickCell(location)

# create dict: num -> list of func pointers, all taking current location and num (position will be determined in the func)


def setBomb(board: Board, location: tuple):
    board.setBomb(location)
    rclickCell(location)
    for cell in board.returnNumberedCells(location):
        mclickCell(cell)