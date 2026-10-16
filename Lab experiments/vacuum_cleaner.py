
rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

position = 'A'

while True:
    print("Vacuum cleaner is in room", position)

    if rooms[position] == 'Dirty':
        print("Cleaning room", position)
        rooms[position] = 'Clean'
    else:
        print("Room", position, "is already clean")

    if position == 'A':
        position = 'B'
    else:
        break

print("Final room status:", rooms)