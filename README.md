# Python Ball: 3D Creature Grid Simulator

## Overview

Python Ball is a simple 3D game/simulator where you control a creature moving around inside a 3D grid "world". The simulation uses VPython for real-time 3D visualization. You can move the creature using keyboard controls and watch its position update within the grid.

## Features
- 3D grid world rendered with VPython
- A controllable creature (red sphere) that moves in 6 directions
- Keyboard controls for movement (WASDQE)
- Visual feedback and boundary enforcement

## Controls
- **W**: Move forward (positive Z)
- **S**: Move backward (negative Z)
- **A**: Move left (negative X)
- **D**: Move right (positive X)
- **Q**: Move up (positive Y)
- **E**: Move down (negative Y)

## Requirements
- Python 3.7+
- [VPython](https://vpython.org/)

## Installation
1. Clone this repository or download the files `main.py` and `game.py`.
2. Install the required Python package:

```bash
pip install vpython
```

## Running the Simulator
Run the following command in your terminal:

```bash
python main.py
```

A 3D window will open. Use the WASDQE keys to move the creature around the grid.

## File Descriptions
- `main.py`: Entry point. Sets up the grid, creature, and handles user input.
- `game.py`: Contains the `creature` and `grid` classes, manages the world and movement logic.

## Notes
- The grid is 10x10x10 units. The creature cannot move outside this boundary.
- The simulation window must be focused for keyboard controls to work.

## License
This project is provided as-is for educational and demonstration purposes.
