
def minimax(tree, depth, maximizing):
    if isinstance(tree, int):
        return tree

    if maximizing:
        best = float("-inf")
        for child in tree:
            best = max(best, minimax(child, depth + 1, False))
        return best
    else:
        best = float("inf")
        for child in tree:
            best = min(best, minimax(child, depth + 1, True))
        return best

tree = [
    [3, 5],
    [2, 9]
]

print("Best value:", minimax(tree, 0, True))
