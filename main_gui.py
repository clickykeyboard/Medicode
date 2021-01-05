from tkinter import *


class MainApplication(Tk):

    def __init__(self, title, icon_path):
        super().__init__()
        self.title(title)
        self.iconbitmap(icon_path)
        self.minsize(400, 400)

        self.mainloop()


main_window = MainApplication("Medicode", "hospital.ico")
