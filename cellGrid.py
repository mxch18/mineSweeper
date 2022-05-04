import tkinter
import math
from PIL import Image, ImageTk
from cell import Cell
from random import shuffle as rshuffle
from os import listdir


class CellGrid(tkinter.Frame):
    def __init__(self, nbCol, nbRow, nbMines, *args, **kwargs):
        tkinter.Frame.__init__(self, name='cell_grid', *args, **kwargs)
        self.place(x=0, y=0)
        # self.grid_propagate(False)
        self.update()

        # Store all images used on cells
        mineHeightWidth = math.floor(
            min(
                self.winfo_width()/nbCol,
                self.winfo_height()/nbRow
            )
        )
        self.imageDict = {}
        for imageFileName in listdir('./images'):
            # Open image
            pilImage = Image.open(f'images/{imageFileName}')
            # Resize image
            pilImage_resized = pilImage.resize(
                (mineHeightWidth-4, mineHeightWidth-4)
            )
            # Convert PIL image into Tkinter image and store the object
            tkImage = ImageTk.PhotoImage(pilImage_resized)
            self.imageDict[imageFileName.split(sep='.')[0]] = tkImage

        self.cellGrid = [
            [
                Cell(
                    x,
                    y,
                    master=self,
                    image=self.imageDict['0'],
                    bd=0,
                    relief=tkinter.FLAT
                )
                for y in range(nbCol)
            ]
            for x in range(nbRow)
        ]
        self.nbRow = nbRow
        self.nbCol = nbCol
        self.isFirstClick = 1
        self.nbMines = nbMines
        self.nbOfFlagsUsed = tkinter.StringVar(
            self, f'0/{self.nbMines}', 'nbOfFlagsUsed'
        )
        self.nbOpenedCells = 0

    def createMinefield(self, btnRow, btnCol):
        self.isFirstClick = 0
        zerosAndOnes = [
            *[1 for x in range(self.nbMines)],
            *[0 for y in range(self.nbRow*self.nbCol - self.nbMines - 1)]
        ]
        rshuffle(zerosAndOnes)
        for row, cellRow in enumerate(self.cellGrid):
            for col, cell in enumerate(cellRow):
                if ((row, col) != (btnRow, btnCol)) and zerosAndOnes.pop(0):
                    cell.setMine()

    def mineSweep(self, btnRow, btnCol):
        cell = self.cellGrid[btnRow][btnCol]
        if cell.isMine:
            cell.configure(bg='red')
            self.endGame(False)
        else:
            idxsToCheck = [(btnRow, btnCol)]
            while len(idxsToCheck):
                idx = idxsToCheck.pop(0)
                cellToCheck = self.cellGrid[idx[0]][idx[1]]

                if cellToCheck['state'] == tkinter.DISABLED:
                    continue

                cellToCheck.configure(state='disabled')
                self.nbOpenedCells += 1
                if self.nbOpenedCells == self.nbRow*self.nbCol-self.nbMines:
                    self.endGame(True)
                nbOfMinesAround, newIdxs = self.countMinesAround(
                    idx[0], idx[1])

                if nbOfMinesAround:
                    cellToCheck.configure(
                        image=self.imageDict[f'{nbOfMinesAround}']
                    )
                else:
                    idxsToCheck += newIdxs

    def endGame(self, bool_victory):
        if bool_victory:
            self.nbOfFlagsUsed.set('YOU WIN!')
        else:
            self.nbOfFlagsUsed.set('YOU LOSE!')

        for w in self.winfo_children():
            if isinstance(w, Cell) and w['state'] != tkinter.DISABLED:
                w.configure(state="disabled")
                w.unbind('<Button-1>')
                w.unbind('<Button-3>')
                if w.isMine:
                    if not w.isFlag:
                        w.configure(image=self.imageDict['bomb'])
                    else:
                        w.configure(bg='green')
                elif w.isFlag:
                    w.configure(bg='red')

    def isEnoughFlags(self):
        nbOfFlagsUsed = int(self.nbOfFlagsUsed.get().split(sep='/')[0])
        return nbOfFlagsUsed < self.nbMines

    def increaseNbOfFlagsUsed(self):
        nbOfFlagsUsed = int(self.nbOfFlagsUsed.get().split(sep='/')[0])
        if nbOfFlagsUsed < self.nbMines:
            self.nbOfFlagsUsed.set(f'{nbOfFlagsUsed+1}/{self.nbMines}')

    def decreaseNbOfFlagsUsed(self):
        nbOfFlagsUsed = int(self.nbOfFlagsUsed.get().split(sep='/')[0])
        if nbOfFlagsUsed > 0:
            self.nbOfFlagsUsed.set(f'{nbOfFlagsUsed-1}/{self.nbMines}')

    def getAdjacentIdx(self, row, col):
        rowAdjacent = CellGrid.getAdjacent(row, self.nbRow)
        colAdjacent = CellGrid.getAdjacent(col, self.nbCol)
        # Make combinations
        idxsToCheck = [(x, y) for x in rowAdjacent for y in colAdjacent]
        idxsToCheck.remove((row, col))

        return idxsToCheck

    def countMinesAround(self, row, col):
        idxsToCheck = self.getAdjacentIdx(row, col)
        # Explore combinations
        nbOfMinesAround = 0
        for idxs in idxsToCheck:
            nbOfMinesAround += self.cellGrid[idxs[0]][idxs[1]].isMine

        return nbOfMinesAround, idxsToCheck

    @staticmethod
    def getAdjacent(rowOrCol, limit):
        res = [rowOrCol]
        if rowOrCol-1 >= 0:
            res.append(rowOrCol-1)
        if rowOrCol+1 < limit:
            res.append(rowOrCol+1)

        return res

    def getNbOfMines(self):
        return self.nbMines


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry('900x700')
    root.configure(bg='black')
    root.title('Mine Sweeper Game')
    root.resizable(False, False)
    root.update()
    a = CellGrid(8, 8, 10, root, bg='blue', height=root.winfo_height(),
                 width=root.winfo_width())
    root.mainloop()
