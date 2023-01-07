from Cell import Cell

class Board(list):
    def __init__(self, size: tuple):
        self.width, self.height = size
        super().__init__()
        # init all cells
        for i in range(size[0]):
            self.append([])
            for j in range(size[1]):
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

    def setBomb(self, location: tuple):
        x, y = location
        self[x][y].setBomb()

    def setValue(self, location: tuple, num: int):
        x, y = location
        self[x][y].setValue(num)

    def get_list_near_coords(self, location: tuple) -> list:
        # x, y 0-index coords
        x, y = location
        cells = []
        local_offset = [-1, 0, 1]
        for i in local_offset:
            for j in local_offset:
                if (i < 0 or i > self.width) or (j < 0 or j > self.height) or (i == 0 and j == 0):
                    continue
                cells.append(self[x + i][y + j])
        return cells
