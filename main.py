from famnit_gym.envs import mill
from famnit_gym.wrappers.mill import Video


from mini_max import *
import random



def ai_move(model, player, opponent, difficulty):

    difficulty_depth = {"easy": 1, "medium": 2, "hard": 3}

    legal_moves = model.legal_moves(player)
    if not legal_moves:
        return None

    # Small chance for randomness
    if random.random() < 0.05:
        return random.choice(legal_moves)

    depth = difficulty_depth[difficulty]
    move, _ = minimax(model, 0, player, opponent, True, float('-inf'), float('inf'), max_depth=depth)
    return move


def get_players(agent):
    player = 1 if agent == "player_1" else 2
    return player, 2 if player == 1 else 1


def game_result(agent, reward):
    if reward > 0:
        return f" {agent} wins!"
    elif reward < 0:
        return f" {agent} loses!"
    return "draw!"


def run_game(difficulty_p1="easy", difficulty_p2="medium", render=False):
    env = mill.env(render_mode="human" if render else None)
    #env = Video(env, filename='mill.mp4')
    env.reset()



    for agent in env.agent_iter():
        obs, reward, terminated, truncated, info = env.last()
        if terminated or truncated:
            return "draw" if reward == 0 else ("player_1" if reward > 0 else "player_2")

        #model = mill.transition_model(env.env)
        model = mill.transition_model(env)
        player, opponent = get_players(agent)
        difficulty = difficulty_p1 if player == 1 else difficulty_p2

        move = ai_move(model, player, opponent, difficulty)
        if move is None:
            return "draw"

        env.step(move)






if __name__ == "__main__":
    run_game("hard", "hard", True)

