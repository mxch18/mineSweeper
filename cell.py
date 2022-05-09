import tkinter


class Cell(tkinter.Button):
    def __init__(self, grid_row, grid_col, *args, **kwargs):
        tkinter.Button.__init__(self, *args, **kwargs)
        self.grid(row=grid_row, column=grid_col)
        self.bind('<Button-1>', self.cmd_left_click_btn)
        self.bind('<Button-3>', self.cmd_right_click_btn)

        self.is_mine = False
        self.is_flag = False

    def cmd_left_click_btn(self, event):
        info_btn = self.grid_info()

        if info_btn['in'].is_first_click:
            # Create minefield
            info_btn['in'].create_mine_field(
                *[info_btn.get(key) for key in ('row', 'column')]
            )

        info_btn['in'].mine_sweep(
            *[info_btn.get(key) for key in ('row', 'column')]
        )

    def cmd_right_click_btn(self, event):
        info_btn = self.grid_info()
        # Set image to flag, or remove flag
        if self.is_flag:
            self.configure(image=info_btn['in'].image_dict['0'])
            info_btn['in'].decrease_nb_of_flags_used()
            self.is_flag = 0
        elif self['state'] == tkinter.ACTIVE and info_btn['in'].is_enough_flags():
            self.configure(image=info_btn['in'].image_dict['flag'])
            info_btn['in'].increase_nb_of_flags_used()
            self.is_flag = 1

    def set_mine(self):
        self.is_mine = 1
