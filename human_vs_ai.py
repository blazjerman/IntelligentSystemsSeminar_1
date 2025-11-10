from main import *
from famnit_gym.wrappers.mill import UserInteraction

def play_human_vs_ai(difficulty="medium"):

    print(f"\nYou are Player 1 (Human) vs {difficulty.upper()} AI (Player 2)")
    env = UserInteraction(mill.env(render_mode="human"))
    env.reset()

    for agent in env.agent_iter():
        obs, reward, terminated, truncated, info = env.last()
        if terminated or truncated:
            print(game_result(agent, reward))
            break

        player, opponent = get_players(agent)

        if agent == "player_1":
            move = get_human_move(env, info)
            if move is None:
                print("User quit interactively!")
                break
            env.step(move)
        else:
            model = mill.transition_model(env.unwrapped)
            move = ai_move(model, player, opponent, difficulty)
            env.step(move)
            print(f"\n AI plays: {move}")


def get_event(env):
    event = env.interact()
    if event["type"] == "quit" or (event["type"] == "key_press" and event["key"] == "escape"):
        raise ValueError('This is not an error it is alternative to sys.exit() XD')
    return event

def get_human_move(env, info):
    move = None
    phase = info["phase"]
    legal_moves = info["legal_moves"]

    selected_piece = None

    if phase == "placing":

        for _, dst, _ in legal_moves:
            env.mark_position(dst, (255, 255, 0, 128))

        while move is None:
            event = get_event(env)
            if event["type"] == "mouse_click":
                for src, dst, cap in legal_moves:
                    if dst == event["position"]:
                        move = [src, dst, cap]
                        break

    else:
        movable_positions = {src for src, _, _ in legal_moves if src != 0}
        for pos in movable_positions:
            env.mark_position(pos, (0, 0, 255, 128))

        while selected_piece is None:
            event = get_event(env)
            if event["type"] == "mouse_click" and event["position"] in movable_positions:
                selected_piece = event["position"]

        env.clear_markings()

        possible_destinations = [(dst, cap) for src, dst, cap in legal_moves if src == selected_piece]
        for dst, _ in possible_destinations:
            env.mark_position(dst, (255, 255, 0, 128))

        while move is None:
            event = get_event(env)
            if event["type"] == "mouse_click":
                for dst, cap in possible_destinations:
                    if dst == event["position"]:
                        move = [selected_piece, dst, cap]
                        break

    env.clear_markings()

    if move and move[2] != 0:

        possible_captures = [cap for src, dst, cap in legal_moves if src == move[0] and dst == move[1] and cap != 0]

        if possible_captures:
            for cap in possible_captures:
                env.mark_position(cap, (255, 0, 0, 128))

            while True:
                event = get_event(env)
                if event["type"] == "mouse_click" and event["position"] in possible_captures:
                    move[2] = event["position"]
                    break

    env.clear_markings()
    return move




if __name__ == "__main__":
    play_human_vs_ai("hard")
