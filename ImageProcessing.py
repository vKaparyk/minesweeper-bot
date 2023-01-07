from PIL import ImageGrab

from config import DIFFICULTY, COLOR_DICT
from Board import Board

# image = ImageGrab.grab(bbox=DIFFICULTY[1])

# image.show()

# image = ImageGrab.grab(bbox=DIFFICULTY[1])

# image.show()

def update_board(board: Board):
    CENTER_SQUARE_SIZE = 6
    CELL_SIZE = 50
    INITIAL_OFFSET = (CELL_SIZE - CENTER_SQUARE_SIZE) / 2 - 1 
    board_size, screen_size, _ = DIFFICULTY
    current_screen = ImageGrab.grab(bbox=screen_size)
    current_screen = current_screen.load()
    
    width, height = board_size
    
    for x in range(width):
        for y in range(height):
            if board[x][y].known:
                continue
            
            for w in range(CENTER_SQUARE_SIZE):
                for h in range(CENTER_SQUARE_SIZE):
                    pixel = current_screen[x * CELL_SIZE + INITIAL_OFFSET + w, y * CELL_SIZE + INITIAL_OFFSET + h]
                    if pixel in COLOR_DICT:
                        board.setValue((w, h), COLOR_DICT.get(pixel))
                        continue
                    
                    
                    print(pixel)
        
            # scan image, set cell properly
            # if color, set number
            # else if white corner, then ?
            # else if gray center, then set number 0
            # else TBD,
    
    