



def evaluate(model, player, opponent):
    return (100 * (model.count_pieces(player) - model.count_pieces(opponent)) +
            (len(model.legal_moves(player)) - len(model.legal_moves(opponent))))


def minimax(model, depth, player, opponent, maximizing, alpha, beta, max_depth=4):
    if depth >= max_depth or model.game_over():
        return None, evaluate(model, player, opponent)

    current_player = player if maximizing else opponent
    legal_moves = model.legal_moves(current_player)

    if not legal_moves:
        return None, float('-inf') if maximizing else float('inf')

    best_move = None

    if maximizing:
        best_value = float('-inf')
        for move in legal_moves:
            new_model = model.clone()
            new_model.make_move(current_player, move)
            _, value = minimax(new_model, depth + 1, player, opponent, False, alpha, beta, max_depth)
            if value > best_value:
                best_value, best_move = value, move
            alpha = max(alpha, value)
            if beta <= alpha:
                break
    else:
        best_value = float('inf')
        for move in legal_moves:
            new_model = model.clone()
            new_model.make_move(current_player, move)
            _, value = minimax(new_model, depth + 1, player, opponent, True, alpha, beta, max_depth)
            if value < best_value:
                best_value, best_move = value, move
            beta = min(beta, value)
            if beta <= alpha:
                break

    return best_move, best_value
