class Cell:
    def __init__(self, location: tuple):
        self.known = False
        self.isBomb = False
        self.count = 0
        self.local_count = 0
        self.location = location

    def __str__(self):
        if self.isBomb:
            return "X"
        elif not self.known:
            return " "
        return str(self.count) if self.count else "0"

    def setValue(self, num: int):
        self.count = num
        self.local_count = num
        self.known = True

    def setBomb(self):
        self.known = True
        self.isBomb = True
        self.count = -1
        self.local_count = -1

    def bombNear(self):
        if not self.isBomb:
            self.count += 1
            self.local_count += 1
