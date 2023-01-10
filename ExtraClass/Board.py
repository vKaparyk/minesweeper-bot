from ExtraClass.Cell import Cell
from ExtraClass.NearbyCells import NearbyCells


class Board(dict):
    def __init__(self, size: tuple, bomb_count: int):
        self.width, self.height = size
        self.bomb_count = bomb_count
        super().__init__()
        # init all cells
        for i in range(self.width):
            for j in range(self.height):
                self[(i, j)] = Cell((i, j))

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
        nearby_cells = NearbyCells(self, location)
        for cell in nearby_cells:
            if cell.known and not cell.isBomb:
                cell.local_count -= 1

    def setValue(self, location: tuple, num: int):
        self[location].setValue(num)

    def getAllLocalNumbers(self) -> list:
        all_nums = []
        for i in self:
            cell = self.get(i)
            if cell.isBomb or not cell.known or not cell.local_count:
                continue
            all_nums.append(i)
        return all_nums

    def returnNumberedCells(self, location: tuple) -> list:
        numbered_cells = []
        nearby = NearbyCells(self, location)
        for cell in nearby:
            if cell.known and not cell.isBomb and cell.count > 0:
                numbered_cells.append(cell.location)
        return numbered_cells
