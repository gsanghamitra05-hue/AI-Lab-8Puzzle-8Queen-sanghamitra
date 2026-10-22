def alphabeta(depth, node, maximizing, alpha, beta, values):
    if depth == 2:
        return values[node]

    if maximizing:
        best = float("-inf")

        for child in [node * 2, node * 2 + 1]:
            value = alphabeta(
                depth + 1, child, False, alpha, beta, values
            )
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float("inf")

        for child in [node * 2, node * 2 + 1]:
            value = alphabeta(
                depth + 1, child, True, alpha, beta, values
            )
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

values = [3, 5, 2, 9]

print("Best value:", alphabeta(
    0, 0, True, float("-inf"), float("inf"), values
))
