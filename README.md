# Maze Solver & Generator

A visual maze generator and solver built in Python using **Tkinter**.  
This project demonstrates core algorithmic concepts such as **Depth-First Search (DFS)**, **Prim’s Algorithm**, and **graph traversal**, with real-time visualization.


## Features

- Maze generation using:
  - Prim’s Algorithm (randomized)
-  Maze solving using DFS with backtracking
-  Real-time visualization of:
  - Maze construction
  - Pathfinding (forward + backtracking)
-  Configurable animation speed
-  Unit-tested core logic (no GUI dependency)


## Demo

![Maze Demo](assets/demo.GIF)



##  Project Structure
```
maze-solver/
├── src/
│ └── maze_solver/
│ ├── app.py # Entry point
│ ├── maze.py # Maze logic (generation + solving)
│ ├── cell.py # Cell representation
│ ├── geometry.py # Point and Line primitives
│ ├── window.py # Tkinter window abstraction
│ └── config.py # Animation timing config
├── tests/
│ └── test_maze.py # Unit tests
├── pyproject.toml
├── README.md
└── .gitignore
```

##  Algorithms Used

### Maze Generation (Prim’s Algorithm)

- Start from an initial cell
- Maintain a list of frontier edges
- Randomly pick a frontier edge
- If it connects to an unvisited cell:
  - Break the wall
  - Add the new cell’s neighbors to the frontier
- Continue until all cells are visited

This produces **dense, natural-looking mazes with many short branches**.

---

### Maze Solving (Depth-First Search)

- Start at the entrance
- Recursively explore valid paths
- Mark cells as visited
- Backtrack when hitting dead ends

Visualization:
- 🔴 Red → forward path
- ⚪ Gray → backtracking

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/maze-solver.git
cd maze-solver
```
### 2. Create a virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux / macOS
```
### 3. Install the project
```bash
python3 -m pip install -e .
```
### 4. Running the Application
**Option 1: CLI (recommended)**
```bash
maze-solver
```
**Option 2: Run as module**
```bash
python3 -m maze_solver.app
```
**Option 3: Direct execution**
```bash
python3 src/maze_solver/app.py
```
**Running Tests**
```bash
python3 -m unittest
```
Tests cover:

- Grid creation
-Entrance/exit correctness
- Visited state reset
- Maze structure integrity

## Configuration

Edit config.py:
```bash
generation_delay = 0.001
solve_delay = 0.05
```
- Lower = faster execution
- Higher = slower (better visualization)

## Visualization Details
- Walls → Thick black lines
- Path (forward) → Red
- Backtracking → Gray
- Cells → Dynamically drawn grid

## Future Improvements
 - Add more generation algorithms (DFS, Kruskal’s)
 - Maze export (image / JSON)
 - Adjustable maze size via CLI
 - Interactive UI controls
 - Performance optimizations
 - Add A* pathfinding

## Concepts Demonstrated
- Graph traversal (DFS)
- Randomized algorithms (Prim’s)
- Backtracking
- Object-oriented design
- Separation of concerns
- Visualization of algorithms

## License

**MIT License**
