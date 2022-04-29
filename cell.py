class Cell:
    def __init__(self, isMine=False):
        self.isMine = isMine


def createCellGrid(nbCol, nbRow):
    return [[Cell() for y in range(nbCol)] for x in range(nbRow)]


if __name__ == '__main__':
    a = createCellGrid(5, 6)
