def board_to_str(board: list) -> str:
    board_str = ""

    board_width = len(board)
    board_height = len(board[0])
    
    HORIZONTAL_SEPARATOR = "-" * (board_width * 3 + (board_width + 1)) + "\n"
    board_str += HORIZONTAL_SEPARATOR
    for y in range(board_height):
        board_str += "|"
        for x in range(board_width):
            display = board[x][y] or " "
            board_str += f" {display} |"
        board_str += "\n"
        board_str += HORIZONTAL_SEPARATOR

    return board_str.strip()

def print_board(board: list) -> None:
    print(board_to_str(board))