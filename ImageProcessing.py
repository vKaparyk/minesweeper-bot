from PIL import ImageGrab

from config import DIFFICULTY, COLOR_DICT, BLACK_COLOR_DICT
from Board import Board
from FoundException import Found


def update_board(board: Board) -> list:
    CENTER_SQUARE_SIZE = 6
    # TODO: apparently, it's very precise. no need to scan such large square
    CELL_SIZE = 50
    INITIAL_OFFSET = (CELL_SIZE - CENTER_SQUARE_SIZE) / 2 - 1
    board_size, screen_size, _ = DIFFICULTY
    width, height = board_size

    new_cells: list = []

    current_screen = ImageGrab.grab(bbox=screen_size)
    current_screen = current_screen.load()

    for x in range(width):
        for y in range(height):
            if board[(x, y)].known:
                continue
            found: bool = False
            # check for 1 - 6 (possibly 8 later)
            for w in range(CENTER_SQUARE_SIZE):
                for h in range(CENTER_SQUARE_SIZE):
                    pixel = current_screen[
                        x * CELL_SIZE + INITIAL_OFFSET + w,
                        y * CELL_SIZE + INITIAL_OFFSET + h,
                    ]
                    if pixel in COLOR_DICT:
                        board.setValue((x, y), COLOR_DICT.get(pixel))
                        new_cells.append((x, y))
                        found = True
                        break
                if found:
                    break
            if found:
                continue

            # check for 7 at different location
            for w in range(CENTER_SQUARE_SIZE):
                for h in range(CENTER_SQUARE_SIZE):
                    pixel = current_screen[
                        x * CELL_SIZE + INITIAL_OFFSET + w, y * CELL_SIZE + 10 + h
                    ]
                    if pixel in BLACK_COLOR_DICT:
                        board.setValue((x, y), COLOR_DICT.get(pixel))
                        new_cells.append((x, y))
                        found = True
                        break
                if found:
                    break
            if found:
                continue

            # check for unknown (white TL corner)
            for w in range(CENTER_SQUARE_SIZE):
                for h in range(CENTER_SQUARE_SIZE):
                    pixel = current_screen[x * CELL_SIZE + 1 + w, y * CELL_SIZE + 1 + h]
                    if pixel == (255, 255, 255):
                        found = True
                        break
                if found:
                    break
            if found:
                continue

            # set to 0 if grey exists
            for w in range(CENTER_SQUARE_SIZE):
                for h in range(CENTER_SQUARE_SIZE):
                    pixel = current_screen[
                        x * CELL_SIZE + INITIAL_OFFSET + w,
                        y * CELL_SIZE + INITIAL_OFFSET + h,
                    ]
                    if pixel == (189, 189, 189):
                        board.setValue((x, y), 0)
                        found = True
                        break
                if found:
                    break

    return new_cells