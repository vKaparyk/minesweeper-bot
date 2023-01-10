from ExtraClass.Cell import Cell

class NearbyCells(list):
    
    def __init__(self, board, location: tuple):
        super().__init__()
        self.unknown_cells_pos = []
        self.bombs = []
        x, y = location
        for j in [-1, 0, 1]:
            for i in [-1, 0, 1]:
                cell = board.get((x + i, y + j), None)
                if not cell or (not i and not j):
                    continue
                self.addCell(cell)
        
    def addCell(self, cell: Cell):
        self.append(cell)
        if cell.isBomb:
            self.bombs.append(cell.location)
        if not cell.known:
            self.unknown_cells_pos.append(cell.location)
            
    def update(self):
        self.unknown_cells_pos = []
        self.bombs = []
        for cell in self:
            if not cell.known:
                self.unknown_cells_pos.append(cell.location)
            if cell.isBomb:
                self.bombs.append(cell.location)