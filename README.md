# AI Puzzle Solver: A* Algorithm Implementation on a 7-tile Puzzle

In this project we apply the power of artificial intelligence to solve a classic 7-tile puzzle using the A* search algorithm. This project not only strengthens our grasp on state space generation and efficient search algorithms but also demonstrates the practical application of AI in solving complex problems.

## Project Highlights

This project is centered on the 7-tile puzzle, a variant of the popular 8-tile puzzle from the 1870s. The challenge involves maneuvering tiles on a 3x3 grid until they're in order, leveraging the A* algorithm to determine the most efficient path to the solution.

## How it Works

The puzzle is navigated by moving one tile at a time, horizontally or vertically. All tiles are confined within the 3x3 grid. To solve the puzzle, we generate a state space and use the A* search algorithm to determine the most effective sequence of moves. The Python code for this application resides in a file named `funny_puzzle.py`.

## Key Components

1. **Priority Queue**: Leveraging the `heapq` Python package, we handle the order of states to be processed based on their associated cost.

2. **Heuristic Function**: The heuristic function `h(s)` computes the sum of Manhattan distances of each tile from its goal position, aiding in the efficiency of the A* search algorithm.

3. **Python Functions**: The two primary functions, `print_succ(state)` and `solve(state)`, respectively print all possible successor states of the puzzle and perform the A* search algorithm to find the solution path.

This project is an excellent representation of the power of AI in problem-solving, offering valuable insights into the use of heuristic functions, priority queues, and state space generation.

## Intriguing Features

Think about this: Can you prove that every starting configuration is solvable? While this isn't a requirement of the project, it's an interesting problem to ponder.

## How to Run

Simply execute the `funny_puzzle.py` Python script, and the program will take care of the rest. The script includes detailed comments explaining the functionality of each code block, which should aid in understanding the program's flow.
