from Cell import Cell


class Board(dict):
    def __init__(self, size: tuple, bomb_count: int):
        self.width, self.height = size
        self.bomb_count = bomb_count
        super().__init__()
        # init all cells
        for i in range(self.width):
            for j in range(self.height):
                self[(i, j)] = Cell()

    def __str__(self):
        board_str = ""
        HORIZONTAL_SEPARATOR = "-" * (self.width * 3 + (self.width + 1)) + "\n"

        board_str += HORIZONTAL_SEPARATOR
        for y in range(self.height):
            board_str += "|"
            for x in range(self.width):
                board_str += f" {self[(x, y)]} |"
            board_str += "\n"
            board_str += HORIZONTAL_SEPARATOR
        return board_str.strip()

    def setBomb(self, location: tuple):
        self[location].setBomb()

    def setValue(self, location: tuple, num: int):
        self[location].setValue(num)

    def get_list_near_coords(self, location: tuple) -> list:
        # x, y 0-index coords
        x, y = location
        cells = []
        local_offset = [-1, 0, 1]
        for i in local_offset:
            for j in local_offset:
                cells.append(self[(x + i, y + j)])
        return cells
