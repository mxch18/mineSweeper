import tkinter
from PIL import Image, ImageTk
import settings
from cellGrid import CellGrid


class InfoPage(tkinter.Frame):
    def __init__(self, cells_width, text_stringVar, *args, **kwargs):
        tkinter.Frame.__init__(self, *args, **kwargs)

        parent = self.nametowidget(self.winfo_parent())
        self.configure(
            width=parent.winfo_width()-cells_width,
            height=parent.winfo_height()
        )
        self.place(x=cells_width, y=0)
        self.update()
        self.grid_propagate(False)

        self.widgetDict = {}

        # Flag image
        pilImage = Image.open('images/flag.png')
        # Resize image
        sizeImg = self.winfo_width()
        pilImage_resized = pilImage.resize((sizeImg, sizeImg))
        # Convert PIL image into Tkinter image and store the object
        tkImage = ImageTk.PhotoImage(pilImage_resized)
        self.imageContainer = tkImage

        # Flag label
        self.widgetDict['labelFlag'] = tkinter.Label(
            self,
            image=self.imageContainer,
            text='faf',
            font=settings.FONT_INFO,
            compound=tkinter.TOP
        )
        self.widgetDict['labelFlag'].grid(row=0, column=0)

        self.widgetDict['restart'] = tkinter.Button(
            self,
            font=settings.FONT_INFO,
            text='Restart'
        )
        self.widgetDict['restart'].grid(row=1, column=0)

        self.widgetDict['change_diff'] = tkinter.Button(
            self,
            font=settings.FONT_INFO,
            text='Change difficulty'
        )
        self.widgetDict['change_diff'].grid(row=2, column=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=2)

    def setCmdBtn(self, btn_name, func):
        self.widgetDict[btn_name].configure(command=func)

    def setTextvariableLabel(self, text_stringVar):
        self.widgetDict['labelFlag'].configure(
            textvariable=text_stringVar
        )


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry('900x700')
    root.configure(bg='black')
    root.title('Mine Sweeper Game')
    root.resizable(False, False)
    root.update()

    b = CellGrid(5, 5, 10, root, bg='blue', height=root.winfo_height(),
                 width=root.winfo_width())
    b.update()

    a = InfoPage(b.winfo_width(), '', root)
    root.mainloop()
