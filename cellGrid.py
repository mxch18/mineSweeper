import tkinter
import math
from PIL import Image, ImageTk
from cell import Cell
from random import shuffle as rshuffle
from os import listdir


class CellGrid(tkinter.Frame):
    def __init__(self, nb_col, nb_row, nb_mines, *args, **kwargs):
        tkinter.Frame.__init__(self, name='cell_grid', *args, **kwargs)
        self.place(x=0, y=0)
        # self.grid_propagate(False)
        self.update()

        # Store all images used on cells
        mine_height_width = math.floor(
            min(
                self.winfo_width()/nb_col,
                self.winfo_height()/nb_row
            )
        )
        self.image_dict = {}
        for image_file_name in listdir('./images'):
            # Open image
            pil_image = Image.open(f'images/{image_file_name}')
            # Resize image
            pil_image_resized = pil_image.resize(
                (mine_height_width-4, mine_height_width-4)
            )
            # Convert PIL image into Tkinter image and store the object
            tk_image = ImageTk.PhotoImage(pil_image_resized)
            self.image_dict[image_file_name.split(sep='.')[0]] = tk_image

        self.cell_grid = [
            [
                Cell(
                    x,
                    y,
                    master=self,
                    image=self.image_dict['0'],
                    bd=0,
                    relief=tkinter.FLAT
                )
                for y in range(nb_col)
            ]
            for x in range(nb_row)
        ]
        self.nb_row = nb_row
        self.nb_col = nb_col
        self.is_first_click = 1
        self.nb_mines = nb_mines
        self.nb_of_flags_used = tkinter.StringVar(
            self, f'0/{self.nb_mines}', 'nb_of_flags_used'
        )
        self.nb_opened_cells = 0

    def create_mine_field(self, btn_row, btn_col):
        self.is_first_click = 0
        zeros_and_ones = [
            *[1 for x in range(self.nb_mines)],
            *[0 for y in range(self.nb_row*self.nb_col - self.nb_mines - 1)]
        ]
        rshuffle(zeros_and_ones)
        for row, cell_row in enumerate(self.cell_grid):
            for col, cell in enumerate(cell_row):
                if ((row, col) != (btn_row, btn_col)) and zeros_and_ones.pop(0):
                    cell.set_mine()

    def mine_sweep(self, btn_row, btn_col):
        cell = self.cell_grid[btn_row][btn_col]
        if cell.is_mine:
            cell.configure(bg='red')
            self.end_game(False)
        else:
            idxs_to_check = [(btn_row, btn_col)]
            while len(idxs_to_check):
                idx = idxs_to_check.pop(0)
                cell_to_check = self.cell_grid[idx[0]][idx[1]]

                if cell_to_check['state'] == tkinter.DISABLED:
                    continue

                cell_to_check.configure(state='disabled')
                self.nb_opened_cells += 1
                if self.nb_opened_cells == self.nb_row*self.nb_col-self.nb_mines:
                    self.end_game(True)
                nb_of_mines_around, new_idxs = self.count_mines_around(
                    idx[0], idx[1])

                if nb_of_mines_around:
                    cell_to_check.configure(
                        image=self.image_dict[f'{nb_of_mines_around}']
                    )
                else:
                    idxs_to_check += new_idxs

    def end_game(self, bool_victory):
        if bool_victory:
            self.nb_of_flags_used.set('YOU WIN!')
        else:
            self.nb_of_flags_used.set('YOU LOSE!')

        for w in self.winfo_children():
            if isinstance(w, Cell) and w['state'] != tkinter.DISABLED:
                w.configure(state="disabled")
                w.unbind('<Button-1>')
                w.unbind('<Button-3>')
                if w.is_mine:
                    if not w.is_flag:
                        w.configure(image=self.image_dict['bomb'])
                    else:
                        w.configure(bg='green')
                elif w.is_flag:
                    w.configure(bg='red')

    def is_enough_flags(self):
        nb_of_flags_used = int(self.nb_of_flags_used.get().split(sep='/')[0])
        return nb_of_flags_used < self.nb_mines

    def increase_nb_of_flags(self):
        nb_of_flags_used = int(self.nb_of_flags_used.get().split(sep='/')[0])
        if nb_of_flags_used < self.nb_mines:
            self.nb_of_flags_used.set(f'{nb_of_flags_used+1}/{self.nb_mines}')

    def decrease_nb_of_flags_used(self):
        nb_of_flags_used = int(self.nb_of_flags_used.get().split(sep='/')[0])
        if nb_of_flags_used > 0:
            self.nb_of_flags_used.set(f'{nb_of_flags_used-1}/{self.nb_mines}')

    def get_adjacent_idx(self, row, col):
        row_adjacent = CellGrid.get_adjacent(row, self.nb_row)
        col_adjacent = CellGrid.get_adjacent(col, self.nb_col)
        # Make combinations
        idxs_to_check = [(x, y) for x in row_adjacent for y in col_adjacent]
        idxs_to_check.remove((row, col))

        return idxs_to_check

    def count_mines_around(self, row, col):
        idxs_to_check = self.get_adjacent_idx(row, col)
        # Explore combinations
        nb_of_mines_around = 0
        for idxs in idxs_to_check:
            nb_of_mines_around += self.cell_grid[idxs[0]][idxs[1]].is_mine

        return nb_of_mines_around, idxs_to_check

    @staticmethod
    def get_adjacent(row_or_col, limit):
        res = [row_or_col]
        if row_or_col-1 >= 0:
            res.append(row_or_col-1)
        if row_or_col+1 < limit:
            res.append(row_or_col+1)

        return res

    def get_nb_of_mines(self):
        return self.nb_mines


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
