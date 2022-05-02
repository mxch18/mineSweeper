import tkinter
import math
from PIL import Image, ImageTk
from cell import Cell


class CellGrid(tkinter.Frame):
    def __init__(self, nbCol, nbRow, imageInit, *args, **kwargs):
        tkinter.Frame.__init__(self, *args, **kwargs)
        self.place(x=0, y=0)
        self.grid_propagate(False)
        self.update()

        mineHeightWidth = math.floor(
            min(
                self.winfo_width()/nbCol,
                self.winfo_height()/nbRow
            )
        )
        img_resized = imageInit.resize(
            (mineHeightWidth-4, mineHeightWidth-4)
        )
        img_resized = ImageTk.PhotoImage(img_resized)

        self.cellGrid = [
            [
                Cell(
                    x,
                    y,
                    img_resized,
                    False,
                    master=self,
                    image=img_resized,
                    bd=0,
                    relief=tkinter.FLAT
                )
                for y in range(nbCol)
            ]
            for x in range(nbRow)
        ]

        self.isFirstClick = 0


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry('900x700')
    root.configure(bg='black')
    root.title('Mine Sweeper Game')
    root.resizable(False, False)
    root.update()
    zero = Image.open('images/0.png')
    a = CellGrid(5, 6, zero, root, bg='blue', height=root.winfo_height(),
                 width=root.winfo_width())
    a.place(x=0, y=0)
    root.mainloop()
