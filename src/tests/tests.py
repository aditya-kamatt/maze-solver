import unittest

from maze_solver.maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        cells = getattr(m1, "_Maze__cells")
        self.assertEqual(len(cells), num_cols)
        self.assertEqual(len(cells[0]), num_rows)

    def test_maze_create_small(self):
        num_cols = 3
        num_rows = 2

        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)

        cells = getattr(m1, "_Maze__cells")
        self.assertEqual(len(cells), num_cols)
        self.assertEqual(len(cells[0]), num_rows)

    def test_maze_create_large(self):
        num_cols = 30
        num_rows = 20

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        cells = getattr(m1, "_Maze__cells")
        self.assertEqual(len(cells), num_cols)
        self.assertEqual(len(cells[0]), num_rows)

    def test_maze_create_one_by_one(self):
        num_cols = 1
        num_rows = 1

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        cells = getattr(m1, "_Maze__cells")
        self.assertEqual(len(cells), num_cols)
        self.assertEqual(len(cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        num_cols = 4
        num_rows = 4

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        cells = getattr(m1, "_Maze__cells")
        self.assertFalse(cells[0][0].has_top_wall)
        self.assertFalse(cells[num_cols - 1][num_rows - 1].has_bottom_wall)

    def test_reset_cells_visited(self):
        m1 = Maze(0, 0, 5, 5, 10, 10)

        cells = getattr(m1, "_Maze__cells")
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                self.assertFalse(cells[i][j].visited)

if __name__ == "__main__":
    unittest.main()