from cellGrid import CellGrid
from infoPage import InfoPage


class GamePage():
    def __init__(self, nbCol_, nbRow_, nbMines_, root_, *args, **kwargs):
        self.cells = CellGrid(nbCol=nbCol_, nbRow=nbRow_, nbMines=nbMines_,
                              master=root_, *args, **kwargs)
        self.cells.update()

        self.infos = InfoPage(self.cells.winfo_width(), '', root_)
        self.infos.setCmdBtn('restart', self.resetCellGrid)
        self.infos.setCmdBtn('change_diff', self.returnToMenu)
        self.infos.setTextvariableLabel(self.cells.nbOfFlagsUsed)

    def resetCellGrid(self):
        # Get parent
        parent = self.cells.nametowidget(self.cells.winfo_parent())
        # Destroy widget and all children
        self.cells.destroy()
        # Recreate widget
        self.cells = CellGrid(
            nbCol=self.cells.nbCol,
            nbRow=self.cells.nbRow,
            nbMines=self.cells.nbMines,
            master=parent,
            height=parent.winfo_height(),
            width=parent.winfo_width()
        )

    def returnToMenu(self):
        self.cells.destroy()
        self.infos.destroy()


if __name__ == '__main__':
    import tkinter
    root = tkinter.Tk()
    root.geometry('900x700')
    root.configure(bg='black')
    root.title('Mine Sweeper Game')
    root.resizable(False, False)
    root.update()
    a = GamePage(6, 6, 10, root, bg='blue', height=root.winfo_height(),
                 width=root.winfo_width())
    root.mainloop()
