from Cell import Cell

class Board(list):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().__init__()
        # init all cells
        for i in range(width):
            self.append([])
            for j in range(height):
                self[i].append(Cell())

    def __str__(self):
        board_str = ""
        HORIZONTAL_SEPARATOR = "-" * (self.width * 3 + (self.width + 1)) + "\n"

        board_str += HORIZONTAL_SEPARATOR
        for y in range(self.height):
            board_str += "|"
            for x in range(self.width):
                board_str += f" {self[x][y]} |"
            board_str += "\n"
            board_str += HORIZONTAL_SEPARATOR
        return board_str.strip()

    def setBomb(self, location):
        x, y = location
        self[x][y].setBomb()
