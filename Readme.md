# Overview

This project is a Python-based implementation of the Minimax Algorithm optimized with Alpha-Beta Pruning to solve the zero-sum game of Tic-Tac-Toe. The AI agent (Nexus-Bot) evaluates all possible future board states and uses positional heuristics to play optimally, ensuring it never loses.

# Features

* **Unbeatable AI:** Uses recursive Minimax algorithm with Alpha-Beta Pruning and center-control heuristics for instant, flawless decision making.
* **Game Logging:** Automatically saves match results, timestamps, and move history to a session-specific file (`nexus_session_[DATE].log`).
* **Modular Design:** Enterprise-grade architecture separating logic, UI, logging, and AI components across five distinct Python modules.

# Tools Used

* **Programming Language:** Python 3.x
* **Standard Libraries:** `math` (for infinite bounds in algorithms), `logging` (for session tracking), `datetime` (for timestamping).

# Steps to Install & Run

1. Ensure Python is installed on your system.
2. Clone the Repository: Download or clone the folder containing the `Nexus_TicTacToe_Engine` files.
3. Open your terminal in the project directory.
4. Run the command: `python application_entry.py`

# Testings

### Test A: Functional Gameplay
1. Run the game.
2. Enter a valid grid coordinate (e.g., `A1`, `B2`, `C3`) to place your 'X'.
3. Verify that the 'O' (Nexus AI) responds immediately with its move.

### Test B: AI Intelligence (The "Unbeatable" Test)
1. Play 3 full games.
2. Try to trap the AI using "fork" strategies (creating two simultaneous threats).
3. **Success Criteria:** The AI must either Win or force a Draw. It must NEVER lose.

### Test C: Robustness (Error Handling)
1. Enter an invalid format (e.g., "Z9" or "Hello") instead of a grid coordinate.
2. Try to place a mark on a spot that is already occupied by X or O.
3. **Success Criteria:** The program should print an error message ("Error: Target cell unavailable.") and ask you to try again. It should NOT crash.

### Test D: Logging System
1. Complete a game (Win or Draw).
2. Open the newly generated `nexus_session_[YYYY-MM-DD].log` file in the project folder.
3. **Success Criteria:** The file should contain a step-by-step history of every move made with timestamps, ending with the final session result.
