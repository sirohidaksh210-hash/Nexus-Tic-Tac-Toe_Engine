class NexusRules:
    """Handles the mathematical validation of the game state."""
    WIN_COMBOS = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Cols
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]

    @staticmethod
    def identify_winner(grid_state):
        for combo in NexusRules.WIN_COMBOS:
            if grid_state[combo[0]] == grid_state[combo[1]] == grid_state[combo[2]] != " ":
                return grid_state[combo[0]]
        if " " not in grid_state:
            return "Draw"
        return None

    @staticmethod
    def calculate_heuristic(grid, ai_tag, user_tag):
        """Advanced state evaluation for AI decision making."""
        weight = 0
        for combo in NexusRules.WIN_COMBOS:
            line = [grid[i] for i in combo]
            if line.count(ai_tag) == 2 and line.count(" ") == 1:
                weight += 10
            elif line.count(user_tag) == 2 and line.count(" ") == 1:
                weight -= 10
        return weight
