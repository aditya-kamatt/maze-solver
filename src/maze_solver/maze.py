import time
import random
import maze_solver.config as config

from maze_solver.cell import Cell

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__generation_delay = config.generation_delay
        self.__solve_delay = config.solve_delay

        if seed is not None:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_prim()
        self.__reset_cells_visited()
    
    def __create_cells(self):
        for i in range(self.__num_cols):
            column = []
            for j in range(self.__num_rows):
                column.append(Cell(self.__win))
            self.__cells.append(column)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)
    
    def __draw_cell(self, i, j):
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y

        self.__cells[i][j].draw(x1, y1, x2, y2)

        self.__animate(self.__generation_delay)

    def __animate(self, delay):
        if self.__win is None:
            return
        
        self.__win.redraw()
        time.sleep(delay)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):            # Depth-first traversal
        self.__cells[i][j].visited = True

        while True:
            possible_directions = []

            if i > 0 and not self.__cells[i - 1][j].visited:
                possible_directions.append("left")
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                possible_directions.append("right")
            if j > 0 and not self.__cells[i][j - 1].visited:
                possible_directions.append("up")
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                possible_directions.append("down")
            
            if len(possible_directions) == 0:
                self.__draw_cell(i, j)
                return

            direction = random.choice(possible_directions)

            if direction == "left":
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(i - 1, j)
                self.__break_walls_r(i - 1, j)

            elif direction == "right":
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(i + 1, j)
                self.__break_walls_r(i + 1, j)

            elif direction == "up":
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(i, j - 1)
                self.__break_walls_r(i, j - 1)

            elif direction == "down":
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(i, j + 1)
                self.__break_walls_r(i, j + 1)

    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False

    def __solve_r(self, i, j):
        self.__animate(self.__solve_delay)

        self.__cells[i][j].visited = True

        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True
        
        directions = [
            (i - 1, j, "left"),
            (i + 1, j, "right"),
            (i, j - 1, "up"),
            (i, j + 1, "down"),
        ]

        for next_i, next_j, direction in directions:
            if next_i < 0 or next_i >= self.__num_cols:
                continue
            if next_j < 0 or next_j >= self.__num_rows:
                continue
            if self.__cells[next_i][next_j].visited:
                continue

            if direction == "left" and self.__cells[i][j].has_left_wall:
                continue
            if direction == "right" and self.__cells[i][j].has_right_wall:
                continue
            if direction == "up" and self.__cells[i][j].has_top_wall:
                continue
            if direction == "down" and self.__cells[i][j].has_bottom_wall:
                continue

            self.__cells[i][j].draw_move(self.__cells[next_i][next_j])

            if self.__solve_r(next_i, next_j):
                return True

            self.__cells[i][j].draw_move(self.__cells[next_i][next_j], undo=True)

        return False
    
    def __break_walls_prim(self):
        def add_frontier(i, j):
            if i > 0 and not self.__cells[i - 1][j].visited:
                frontier.append((i, j, i - 1, j))
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                frontier.append((i, j, i + 1, j))
            if j > 0 and not self.__cells[i][j - 1].visited:
                frontier.append((i, j, i, j - 1))
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                frontier.append((i, j, i, j + 1))

        start_i = 0
        start_j = 0

        self.__cells[start_i][start_j].visited = True

        frontier = []
        add_frontier(start_i, start_j)

        while frontier:
            current_i, current_j, next_i, next_j = random.choice(frontier)
            frontier.remove((current_i, current_j, next_i, next_j))

            if self.__cells[next_i][next_j].visited:
                continue

            if next_i == current_i - 1:
                self.__cells[current_i][current_j].has_left_wall = False
                self.__cells[next_i][next_j].has_right_wall = False

            elif next_i == current_i + 1:
                self.__cells[current_i][current_j].has_right_wall = False
                self.__cells[next_i][next_j].has_left_wall = False

            elif next_j == current_j - 1:
                self.__cells[current_i][current_j].has_top_wall = False
                self.__cells[next_i][next_j].has_bottom_wall = False

            elif next_j == current_j + 1:
                self.__cells[current_i][current_j].has_bottom_wall = False
                self.__cells[next_i][next_j].has_top_wall = False

            self.__cells[next_i][next_j].visited = True

            self.__draw_cell(current_i, current_j)
            self.__draw_cell(next_i, next_j)

            add_frontier(next_i, next_j)
    
    def solve(self):
        return self.__solve_r(0, 0)

