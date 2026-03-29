class NexusInterface:
    """Manages the visual representation and coordinate mapping."""
    def __init__(self):
        self.matrix = [" "] * 9
        self.coord_map = {
            'A1': 0, 'A2': 1, 'A3': 2,
            'B1': 3, 'B2': 4, 'B3': 5,
            'C1': 6, 'C2': 7, 'C3': 8
        }

    def render_view(self):
        print("\n    [1] [2] [3]")
        print("  -------------")
        labels = ['A', 'B', 'C']
        for i, label in enumerate(labels):
            start = i * 3
            cells = self.matrix[start:start+3]
            print(f"{label} | " + " | ".join(cells) + " |")
            print("  -------------")

    def apply_move(self, pos, symbol):
        idx = self.coord_map.get(pos.upper())
        if idx is not None and self.matrix[idx] == " ":
            self.matrix[idx] = symbol
            return True
        return False
