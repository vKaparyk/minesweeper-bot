class Cell:
    def __init__(self):
        self.isBomb = False
        self.count = 0
        # self.unknown = True
        # self.pixel_color = 

    def __str__(self):
        if self.isBomb:
            return "X"
        # elif self.unknown:
        #     return "?"
        return str(self.count) if self.count else " "

    def setBomb(self):
        self.isBomb = True
        self.count = -1

    def bombNear(self):
        if not self.isBomb:
            self.count += 1