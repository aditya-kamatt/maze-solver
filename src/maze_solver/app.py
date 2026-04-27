import time
import maze_solver.config as config

from maze_solver.window import Window
from maze_solver.maze import Maze


def main():
    win = Window(800,600)

    time.sleep(config.start_delay)

    maze = Maze(
        50,
        50,
        10,
        12,
        50,
        50,
        win,
        seed=config.seed,
    )
    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()