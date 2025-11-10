from main import *



def tournament(rounds=5):

    matchups = [("easy", "medium"), ("medium", "hard"), ("easy", "hard")]
    results = {}

    for p1, p2 in matchups:
        print(f"\nPlaying {p1.upper()} vs {p2.upper()} ...")
        p1_wins, draws = 0, 0

        for _ in range(rounds):
            winner = run_game(p1, p2)
            if winner == "player_1":
                p1_wins += 1
            elif winner == "draw":
                draws += 1

        win_rate = p1_wins / rounds
        results[(p1, p2)] = (win_rate, draws / rounds)
        print(f"{p1} won {p1_wins}/{rounds} ({win_rate*100:.1f}%), draws {draws}")

    return results



if __name__ == "__main__":
    tournament(rounds=20)
