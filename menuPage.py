import tkinter
import settings
import math
from gamePage import GamePage


class MenuPage(tkinter.Frame):
    def __init__(self, *args, **kwargs):
        tkinter.Frame.__init__(self, *args, **kwargs)

        self.btn_list = {}
        self.pixel_virtual = tkinter.PhotoImage(width=1, height=1)
        self.place(x=0, y=0)
        self.update()

        # 4 buttons : 8x8 (10 mines) , 12x12 (24 mines), 16x16 (40 mines), custom
        btn_height_width = math.floor(
            min(
                self.winfo_width()/2,
                self.winfo_height()/2
            )
        )

        parent = self.nametowidget(self.winfo_parent())
        width_parent = parent.winfo_width()
        height_parent = parent.winfo_height()

        self.btn_list['8x8'] = tkinter.Button(
            self,
            font=settings.FONT,
            image=self.pixel_virtual,
            height=btn_height_width,
            width=btn_height_width,
            compound='c',
            text='8x8\n(10 mines)',
            command=lambda: GamePage(8, 8, 10,
                                     parent,
                                     bg='green',
                                     height=height_parent,
                                     width=width_parent
                                     )
        )

        self.btn_list['12x12'] = tkinter.Button(
            self,
            font=settings.FONT,
            image=self.pixel_virtual,
            height=btn_height_width,
            width=btn_height_width,
            compound='c',
            text='12x12\n(24 mines)',
            command=lambda: GamePage(12, 12, 24,
                                     parent,
                                     bg='green',
                                     height=height_parent,
                                     width=width_parent
                                     )
        )

        self.btn_list['16x16'] = tkinter.Button(
            self,
            font=settings.FONT,
            image=self.pixel_virtual,
            height=btn_height_width,
            width=btn_height_width,
            compound='c',
            text='16x16\n(40 mines)',
            command=lambda: GamePage(16, 16, 40,
                                     parent,
                                     bg='green',
                                     height=height_parent,
                                     width=width_parent
                                     )
        )

        self.btn_list['8x8'].grid(column=0, row=0)
        self.btn_list['12x12'].grid(column=1, row=0)
        self.btn_list['16x16'].grid(
            column=0, row=1, columnspan=2, sticky=tkinter.EW
        )
        self.update()
        self.place(x=(width_parent-self.winfo_width())/2, y=0)


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry('900x700')
    root.configure(bg='grey')
    root.title('Mine Sweeper Game')
    root.resizable(False, False)
    root.update()

    a = MenuPage(root, height=root.winfo_height(),
                 width=math.floor(root.winfo_width()))
    root.mainloop()
