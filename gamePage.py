from cellGrid import CellGrid
from infoPage import InfoPage


class GamePage():
    def __init__(self, nb_col_, nb_row_, nb_mines_, root_, *args, **kwargs):
        self.cells = CellGrid(nb_col=nb_col_, nb_row=nb_row_, nb_mines=nb_mines_,
                              master=root_, *args, **kwargs)
        self.cells.update()

        self.infos = InfoPage(self.cells.winfo_width(), '', root_)
        self.infos.set_cmd_btn('restart', self.reset_cell_grid)
        self.infos.set_cmd_btn('change_diff', self.return_to_menu)
        self.infos.set_textvariable_label(self.cells.nb_of_flags_used)

    def reset_cell_grid(self):
        # Get parent
        parent = self.cells.nametowidget(self.cells.winfo_parent())
        # Destroy widget and all children
        self.cells.destroy()
        # Recreate widget
        self.cells = CellGrid(
            nb_col=self.cells.nb_col,
            nb_row=self.cells.nb_row,
            nb_mines=self.cells.nb_mines,
            master=parent,
            height=parent.winfo_height(),
            width=parent.winfo_width()
        )

    def return_to_menu(self):
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
