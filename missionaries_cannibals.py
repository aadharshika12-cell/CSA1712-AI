from collections import deque

def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False

    if m_left > 0 and m_left < c_left:
        return False

    if m_right > 0 and m_right < c_right:
        return False

    return True


def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque()
    queue.append((start, []))

    visited = set()

    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path + [state]

        m_left, c_left, boat = state

        for m, c in moves:

            if boat == 1:
                new_m = m_left - m
                new_c = c_left - c
                new_boat = 0
            else:
                new_m = m_left + m
                new_c = c_left + c
                new_boat = 1

            new_state = (new_m, new_c, new_boat)

            if is_valid(new_m, new_c) and new_state not in visited:
                queue.append((new_state, path + [state]))

    return None


solution = solve()

if solution:
    print("Missionaries and Cannibals Solution:")
    print()

    for step, state in enumerate(solution):
        m, c, boat = state

        side = "Left" if boat == 1 else "Right"

        print("Step", step)
        print("Missionaries on left:", m)
        print("Cannibals on left:", c)
        print("Boat:", side)
        print()
else:
    print("No solution found.")