from PIL import ImageGrab

from config import DIFFICULTY, COLOR_DICT, BLACK_COLOR_DICT
from ExtraClass.Board import Board


def update_board(board: Board) -> list:
    CELL_SIZE = 50
    HORIZONTAL_OFFSET = 33
    VERTICAL_OFFSET = 36

    board_size, screen_size, _ = DIFFICULTY
    screen_size = screen_size[0] + screen_size[1]
    width, height = board_size

    new_cells: list = []

    current_screen = ImageGrab.grab(bbox=screen_size)
    current_screen = current_screen.load()

    for x in range(width):
        for y in range(height):
            if board[(x, y)].known:
                continue
            # check for 1 - 6 (possibly 8 later)
            pixel = current_screen[
                x * CELL_SIZE + HORIZONTAL_OFFSET,
                y * CELL_SIZE + VERTICAL_OFFSET,
            ]
            if pixel in COLOR_DICT:
                board.setValue((x, y), COLOR_DICT.get(pixel))
                new_cells.append((x, y))
                continue

            # check for 7 at different location
            pixel = current_screen[
                x * CELL_SIZE + HORIZONTAL_OFFSET, y * CELL_SIZE + 10
            ]
            if pixel in BLACK_COLOR_DICT:
                board.setValue((x, y), COLOR_DICT.get(pixel))
                new_cells.append((x, y))
                continue

            # check for unknown (white TL corner)
            pixel = current_screen[x * CELL_SIZE + 1, y * CELL_SIZE + 1]
            if pixel == (255, 255, 255):
                continue

            # set to 0 if grey exists
            pixel = current_screen[
                x * CELL_SIZE + HORIZONTAL_OFFSET,
                y * CELL_SIZE + VERTICAL_OFFSET,
            ]
            if pixel == (189, 189, 189):
                board.setValue((x, y), 0)
                continue

    return new_cells
