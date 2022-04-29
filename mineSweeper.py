import tkinter
import math
import settings
import cell
from PIL import Image, ImageTk


def menuPage(parent):
    page = tkinter.Frame(
        parent,
        bg=settings.BG_COLOR,
        height=parent.winfo_height(),
        width=math.floor(parent.winfo_width()/2)
    )
    page.place(relx=0.25)
    page.update()
    # 4 buttons : 8x8 (10 mines) , 12x12 (24 mines), 16x16 (40 mines), custom
    btnHeightWidth = math.floor(page.winfo_height()/2)
    btn_8x8 = tkinter.Button(
        page,
        font=settings.FONT,
        image=pixelVirtual,
        height=btnHeightWidth,
        width=btnHeightWidth,
        compound='c',
        text='8x8\n(10 mines)'
        )
    btn_16x16 = tkinter.Button(
        page,
        font=settings.FONT,
        image=pixelVirtual,
        height=btnHeightWidth,
        width=btnHeightWidth,
        compound='c',
        text='12x12\n(24 mines)'
        )
    btn_30x16 = tkinter.Button(
        page,
        font=settings.FONT,
        image=pixelVirtual,
        height=btnHeightWidth,
        width=btnHeightWidth,
        compound='c',
        text='16x16\n(40 mines)'
        )

    btn_8x8.grid(column=0, row=0)
    btn_16x16.grid(column=1, row=0)
    btn_30x16.grid(column=0, row=1, columnspan=2, sticky=tkinter.EW)
    return page


def gamePage(parent, nbCol, nbRow):
    frame_mine = tkinter.Frame(
        parent,
        bg='blue',
        width=math.floor(parent.winfo_width()*0.75),
        height=root.winfo_height()
    )
    frame_mine.place(x=0, y=0)
    frame_mine.grid_propagate(False)
    frame_mine.update()
    # Create mine field
    cellGrid = cell.createCellGrid(nbCol, nbRow)  # nbRow x nbCol

    mineHeightWidth = math.floor(
        min(
            frame_mine.winfo_width()/nbCol,
            frame_mine.winfo_height()/nbRow
        )
    )
    zero_resized = zero.resize((mineHeightWidth-4, mineHeightWidth-4))
    zero_resized = ImageTk.PhotoImage(zero_resized)
    for i in range(len(cellGrid)):
        for j in range(len(cellGrid[0])):
            # Create button and grid it
            mine_ij = tkinter.Button(
                frame_mine,
                image=zero_resized,
                bd=0,
                relief=tkinter.FLAT
            )
            mine_ij.grid(column=j, row=i)
            mine_ij.update()
    return frame_mine
    # Information frame
    # frame_information = tkinter.Frame(
    #     root,
    #     bg=settings.BG_COLOR,
    #     width=parent.winfo_width()-frame_mine.winfo_width(),
    #     height=parent.winfo_height()
    # )
    # frame_information.place(
    #     x=frame_mine.winfo_width(),
    #     y=0
    # )


if __name__ == '__main__':
    # Create window
    root = tkinter.Tk()

    # Load images
    pixelVirtual = tkinter.PhotoImage(width=1, height=1)
    zero = Image.open('images/0.png')
    one = Image.open('images/1.png')
    two = Image.open('images/2.png')
    three = Image.open('images/3.png')
    four = Image.open('images/4.png')
    five = Image.open('images/5.png')
    six = Image.open('images/6.png')
    seven = Image.open('images/7.png')
    eight = Image.open('images/8.png')
    flag = Image.open('images/flag.png')
    qmark = Image.open('images/qmark.png')

    # Window settings
    root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
    root.configure(bg='black')
    root.title('Mine Sweeper Game')
    root.resizable(False, False)

    root.update()
    # nbCol, nbRow = 16, 16
    # frame_mine = tkinter.Frame(
    #     root,
    #     bg='blue',
    #     width=math.floor(root.winfo_width()*0.75),
    #     height=root.winfo_height()
    # )
    # frame_mine.place(x=0, y=0)
    # frame_mine.grid_propagate(False)
    # frame_mine.update()
    # # Create mine field
    # cellGrid = cell.createCellGrid(nbCol, nbRow)  # nbRow x nbCol
    #
    # mineHeightWidth = math.floor(
    #     min(
    #         frame_mine.winfo_width()/nbCol,
    #         frame_mine.winfo_height()/nbRow
    #     )
    # )
    # zero_resized = zero.resize((mineHeightWidth-4, mineHeightWidth-4))
    # zero_resized = ImageTk.PhotoImage(zero_resized)
    # for i in range(len(cellGrid)):
    #     for j in range(len(cellGrid[0])):
    #         # Create button and grid it
    #         mine_ij = tkinter.Button(
    #             frame_mine,
    #             image=zero_resized,
    #             bd=0,
    #             relief=tkinter.FLAT
    #         )
    #         mine_ij.grid(column=j, row=i)
    #         mine_ij.update()
    f = gamePage(root, 5, 5)
    # Run the window
    root.mainloop()
