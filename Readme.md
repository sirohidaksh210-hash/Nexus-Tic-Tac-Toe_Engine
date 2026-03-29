# Overview

The Nexus Tic-Tac-Toe Engine is a robust, terminal-based implementation of the classic zero-sum game, engineered to showcase advanced artificial intelligence concepts. Unlike standard random-move bots, the "Nexus-Bot" utilizes a fully optimized Minimax algorithm paired with Alpha-Beta Pruning and positional heuristics. By analyzing entire decision trees and calculating future board states, the engine guarantees an unbeatable AI opponent that will invariably secure a win or force a draw.

# Features

* **Algorithmic Invincibility:** Powered by a recursive Minimax algorithm that is mathematically incapable of losing.
* **Optimized Decision Making:** Implements Alpha-Beta Pruning to ignore redundant game-tree branches, resulting in instant, zero-latency move calculations.
* **Enterprise Logging System:** Automatically tracks and writes all session data—including exact timestamps, user coordinates, and final outcomes—to a dedicated `nexus_session_[DATE].log` file.
* **Modular Architecture:** Adheres to the Single Responsibility Principle by dividing the engine into five distinct modules: Core Engine, Interface Manager, Intelligence Module, System Auditor, and Application Entry.

# Tools Used

* **Programming Language:** Python 3.x
* **Standard Libraries:** * `math` (for establishing infinite bounds in the Alpha-Beta algorithm)
  * `logging` (for asynchronous session auditing)
  * `datetime` (for real-time event tracking)

# Steps to Install & Run

1. Verify that Python 3.x is installed on your local environment.
2. Clone or download the project repository to your machine.
3. Open your terminal or command line interface and navigate to the project directory.
4. Execute the following command to initialize the engine: 
   `python application_entry.py`

# Testings

### Test A: Functional Gameplay & Input Mapping
* **Procedure:** Initialize the game. When prompted, enter a valid alphanumeric coordinate (e.g., `A1`, `B2`, `C3`) to claim a cell.
* **Success Criteria:** The interface must update to reflect the user's 'X', and the Nexus-Bot ('O') must immediately counter-move without crashing.

### Test B: AI Intelligence (The "Unbeatable" Test)
* **Procedure:** Play a minimum of three consecutive matches. Attempt advanced Tic-Tac-Toe tactics, such as setting up a "fork" (creating two unblockable win conditions simultaneously).
* **Success Criteria:** The AI must perfectly predict and block all traps. The session must end in either an AI victory or a Draw. The AI must never register a loss.

### Test C: Robustness & Exception Handling
* **Procedure:** Intentionally input invalid data when prompted. Try entering a string (e.g., "Hello"), an out-of-bounds coordinate (e.g., "Z9"), or a coordinate that is already occupied on the grid.
* **Success Criteria:** The engine must catch the exception, print a clear error message ("Error: Target cell unavailable."), and safely reprompt the user for input without terminating the application.

### Test D: Audit Logging System
* **Procedure:** Complete a full match (Win or Draw). Navigate to the project folder and open the newly generated `.log` file.
* **Success Criteria:** The file must contain a sequential, timestamped ledger of every move executed during the session, concluding with an accurate declaration of the final game state.
