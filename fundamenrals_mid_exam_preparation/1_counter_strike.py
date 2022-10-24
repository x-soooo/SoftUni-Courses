energy = int(input())
count = 0

while True:
    command = input()

    if command == 'End of battle':
        print(f"Won battles: {count}. Energy left: {energy}")
        break

    distance = int(command)

    if energy >= distance:
        energy -= distance
        count += 1

        if count % 3 == 0:
            energy += count
    else:
        print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
        break
