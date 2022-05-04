import tkinter


class Cell(tkinter.Button):
    def __init__(self, gridRow, gridCol, *args, **kwargs):
        tkinter.Button.__init__(self, *args, **kwargs)
        self.grid(row=gridRow, column=gridCol)
        self.bind('<Button-1>', self.cmdLeftClickBtn)
        self.bind('<Button-3>', self.cmdRightClickBtn)

        self.isMine = False
        self.isFlag = False

    def cmdLeftClickBtn(self, event):
        infoBtn = self.grid_info()

        if infoBtn['in'].isFirstClick:
            # Create minefield
            infoBtn['in'].createMinefield(
                *[infoBtn.get(key) for key in ('row', 'column')]
            )

        infoBtn['in'].mineSweep(
            *[infoBtn.get(key) for key in ('row', 'column')]
        )

    def cmdRightClickBtn(self, event):
        infoBtn = self.grid_info()
        # Set image to flag, or remove flag
        if self.isFlag:
            self.configure(image=infoBtn['in'].imageDict['0'])
            infoBtn['in'].decreaseNbOfFlagsUsed()
            self.isFlag = 0
        elif self['state'] == tkinter.ACTIVE and infoBtn['in'].isEnoughFlags():
            self.configure(image=infoBtn['in'].imageDict['flag'])
            infoBtn['in'].increaseNbOfFlagsUsed()
            self.isFlag = 1

    def setMine(self):
        self.isMine = 1
