import math
from game_rules import NexusRules

class NexusAI:
    """Implements Alpha-Beta Pruning for optimal move selection."""
    def __init__(self, ai_symbol):
        self.id = ai_symbol
        self.human_id = "O" if ai_symbol == "X" else "X"

    def get_optimal_coordinate(self, current_matrix):
        best_val = -math.inf
        best_idx = None
        
        for i in range(9):
            if current_matrix[i] == " ":
                current_matrix[i] = self.id
                score = self.alpha_beta(current_matrix, 0, False, -math.inf, math.inf)
                current_matrix[i] = " "
                if score > best_val:
                    best_val = score
                    best_idx = i
        
        rev_map = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
        return rev_map[best_idx]

    def alpha_beta(self, state, depth, is_max, alpha, beta):
        result = NexusRules.identify_winner(state)
        if result == self.id: return 100 - depth
        if result == self.human_id: return depth - 100
        if result == "Draw": return 0

        if is_max:
            val = -math.inf
            for i in range(9):
                if state[i] == " ":
                    state[i] = self.id
                    val = max(val, self.alpha_beta(state, depth + 1, False, alpha, beta))
                    state[i] = " "
                    alpha = max(alpha, val)
                    if beta <= alpha: break
            return val
        else:
            val = math.inf
            for i in range(9):
                if state[i] == " ":
                    state[i] = self.human_id
                    val = min(val, self.alpha_beta(state, depth + 1, True, alpha, beta))
                    state[i] = " "
                    beta = min(beta, val)
                    if beta <= alpha: break
            return val
