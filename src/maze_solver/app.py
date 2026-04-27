import time
import maze_solver.config as config

from src.maze_solver.window import Window
from src.maze_solver.maze import Maze


def main():
    win = Window(800,600)

    maze = Maze(
        50,
        50,
        10,
        12,
        50,
        50,
        win,
        #seed=config.seed,
    )
    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()