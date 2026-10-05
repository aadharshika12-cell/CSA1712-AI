from collections import deque

def water_jug(capacity1, capacity2, target):
    queue = deque()
    visited = set()

    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        if jug1 == target or jug2 == target:
            return path + [(jug1, jug2)]

        states = [
            (capacity1, jug2),
            (jug1, capacity2),
            (0, jug2),
            (jug1, 0)
        ]

        pour = min(jug1, capacity2 - jug2)
        states.append((jug1 - pour, jug2 + pour))

        pour = min(jug2, capacity1 - jug1)
        states.append((jug1 + pour, jug2 - pour))

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path + [(jug1, jug2)]))

    return None


capacity1 = 4
capacity2 = 3
target = 2

solution = water_jug(capacity1, capacity2, target)

if solution:
    print("Water Jug Solution:")

    for step, state in enumerate(solution):
        print("Step", step, ":", state)
else:
    print("No solution found.")