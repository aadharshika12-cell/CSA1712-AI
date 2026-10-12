
def alpha_beta(tree, alpha, beta, maximizing):
    if isinstance(tree, int):
        return tree

    if maximizing:
        best = float("-inf")

        for child in tree:
            value = alpha_beta(child, alpha, beta, False)
            best = max(best, value)
            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:
        best = float("inf")

        for child in tree:
            value = alpha_beta(child, alpha, beta, True)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

tree = [
    [3, 5],
    [2, 9]
]

result = alpha_beta(
    tree, float("-inf"), float("inf"), True
)

print("Best value:", result)
