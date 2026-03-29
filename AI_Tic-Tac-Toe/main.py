from board import NexusInterface
from ai_agent import NexusAI
from game_rules import NexusRules
from logger import NexusLog

def initialize_nexus():
    ui = NexusInterface()
    bot = NexusAI("O")
    auditor = NexusLog()
    turn = "X" # User starts

    print("=== NEXUS TIC-TAC-TOE SYSTEM ONLINE ===")
    
    while True:
        ui.render_view()
        status = NexusRules.identify_winner(ui.matrix)

        if status:
            print(f"\nFinal Status: {status}")
            auditor.finalize(status)
            break

        if turn == "X":
            user_input = input(f"Input Coordinate (A1-C3): ").strip().upper()
            if ui.apply_move(user_input, "X"):
                auditor.record_action("User", user_input)
                turn = "O"
            else:
                print("Error: Target cell unavailable.")
        else:
            print("Nexus AI is computing...")
            ai_move = bot.get_optimal_coordinate(ui.matrix)
            ui.apply_move(ai_move, "O")
            auditor.record_action("Nexus-Bot", ai_move)
            turn = "X"

if __name__ == "__main__":
    initialize_nexus()
