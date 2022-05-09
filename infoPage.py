import tkinter
from PIL import Image, ImageTk
import settings
from cellGrid import CellGrid


class InfoPage(tkinter.Frame):
    def __init__(self, cells_width, text_stringvar, *args, **kwargs):
        tkinter.Frame.__init__(self, *args, **kwargs)

        parent = self.nametowidget(self.winfo_parent())
        self.configure(
            width=parent.winfo_width()-cells_width,
            height=parent.winfo_height()
        )
        self.place(x=cells_width, y=0)
        self.update()
        self.grid_propagate(False)

        self.widget_dict = {}

        # Flag image
        pil_image = Image.open('images/flag.png')
        # Resize image
        sizeImg = self.winfo_width()
        pil_image_resized = pil_image.resize((sizeImg, sizeImg))
        # Convert PIL image into Tkinter image and store the object
        tk_image = ImageTk.PhotoImage(pil_image_resized)
        self.image_container = tk_image

        # Flag label
        self.widget_dict['label_flag'] = tkinter.Label(
            self,
            image=self.image_container,
            text='faf',
            font=settings.FONT_INFO,
            compound=tkinter.TOP
        )
        self.widget_dict['label_flag'].grid(row=0, column=0)

        self.widget_dict['restart'] = tkinter.Button(
            self,
            font=settings.FONT_INFO,
            text='Restart'
        )
        self.widget_dict['restart'].grid(row=1, column=0)

        self.widget_dict['change_diff'] = tkinter.Button(
            self,
            font=settings.FONT_INFO,
            text='Change difficulty'
        )
        self.widget_dict['change_diff'].grid(row=2, column=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=2)

    def set_cmd_btn(self, btn_name, func):
        self.widget_dict[btn_name].configure(command=func)

    def set_textvariable_label(self, text_stringvar):
        self.widget_dict['label_flag'].configure(
            textvariable=text_stringvar
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
