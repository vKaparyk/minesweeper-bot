class Cell:
    def __init__(self):
        self.known = False
        self.isBomb = False
        self.count = 0

    def __str__(self):
        if self.isBomb:
            return "X"
        elif self.known:
            return "?"
        return str(self.count) if self.count else " "

    def setValue(self, num: int):
        self.count = num
        self.known = True

    def setBomb(self):
        self.isBomb = True
        self.count = -1

    def bombNear(self):
        if not self.isBomb:
            self.count += 1