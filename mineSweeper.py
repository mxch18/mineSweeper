import tkinter
import math
import settings

root = tkinter.Tk()

# Window settings
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.configure(bg='black')
root.title('Mine Sweeper Game')
root.resizable(False, False)

root.update()

# Main game frame
frame_mine = tkinter.Frame(
    root,
    bg='red',
    width=math.floor(root.winfo_width()*0.75),
    height=root.winfo_height()
)
frame_mine.place(x=0, y=0)
frame_mine.update()

# Information frame
frame_information = tkinter.Frame(
    root,
    bg='blue',
    width=root.winfo_width()-frame_mine.winfo_width(),
    height=root.winfo_height()
)
frame_information.place(
    x=frame_mine.winfo_width(),
    y=0
)

# Run the window
root.mainloop()
