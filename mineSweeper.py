import tkinter
import settings
from menuPage import MenuPage

if __name__ == '__main__':
    # Create window
    root = tkinter.Tk()

    # Window settings
    root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
    root.configure(bg=settings.BG_COLOR)
    root.title('Mine Sweeper Game')
    root.resizable(False, False)

    root.update()

    MenuPage(root, height=root.winfo_height(), width=root.winfo_width())

    # Run the window
    root.mainloop()
