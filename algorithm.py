
import heapq

grid = [
    ['S', '.', '.', '.'],
    ['#', '#', '.', '#'],
    ['.', '.', '.', '.'],
    ['.', '#', '#', 'G']
]

start = (0, 0)
goal = (3, 3)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

pq = [(heuristic(start, goal), 0, start)]
parent = {}
g_cost = {start: 0}

while pq:
    f, cost, current = heapq.heappop(pq)

    if current == goal:
        break

    r, c = current

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc

        if (0 <= nr < len(grid) and
            0 <= nc < len(grid[0]) and
            grid[nr][nc] != '#'):

            neighbour = (nr, nc)
            new_cost = g_cost[current] + 1

            if new_cost < g_cost.get(neighbour, float('inf')):
                g_cost[neighbour] = new_cost
                parent[neighbour] = current
                f_cost = new_cost + heuristic(neighbour, goal)
                heapq.heappush(
                    pq, (f_cost, new_cost, neighbour)
                )

if goal in g_cost:
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()

    print("Path:", path)
    print("Total cost:", g_cost[goal])
else:
    print("No path found")