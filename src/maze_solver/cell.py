import maze_solver.config as config

from maze_solver.window import Window
from maze_solver.geometry import Point, Line

class Cell:
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.visited = False

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.__win is None:
            return

        bg_color = "#d9d9d9"

        left_color = "black" if self.has_left_wall else bg_color
        right_color = "black" if self.has_right_wall else bg_color
        top_color = "black" if self.has_top_wall else bg_color
        bottom_color = "black" if self.has_bottom_wall else bg_color

        self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), left_color, config.wall_width)
        self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), right_color, config.wall_width)
        self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), top_color, config.wall_width)
        self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), bottom_color, config.wall_width)

    def draw_move(self, to_cell, undo=False):
        x_centre_self = (self.__x1 + self.__x2) / 2
        y_centre_self = (self.__y1 + self.__y2) / 2

        x_centre_to = (to_cell.__x1 + to_cell.__x2) / 2
        y_centre_to = (to_cell.__y1 + to_cell.__y2) / 2

        if self.__win is None:
            return
        

        color = "gray" if undo else "red"

        line = Line(
            Point(x_centre_self, y_centre_self),
            Point(x_centre_to, y_centre_to)
        )

        self.__win.draw_line(line, color, config.path_width)
