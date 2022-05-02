import tkinter


class Cell(tkinter.Button):
    def __init__(self, gridRow, gridCol, imageContainer, isMine=False, *args, **kwargs):
        tkinter.Button.__init__(self, *args, **kwargs)
        self.grid(row=gridRow, column=gridCol)
        self.bind('<Button-1>', self.cmdLeftClickBtn)

        self.isMine = isMine
        self.imageContainer = imageContainer

    def cmdLeftClickBtn(self, event):
        infoBtn = self.grid_info()
        print(f"I am button {infoBtn['row']}x{infoBtn['column']}")
