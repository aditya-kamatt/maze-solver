from tkinter import Tk, Canvas, BOTH

class Window:
    def __init__(self, width: float, height: float):
        self.__root = Tk()
        self.__root.title("Window")

        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.__running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color = "black", width=2):
        line.draw(self.__canvas, fill_color, width)