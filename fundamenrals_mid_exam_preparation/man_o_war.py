pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())
lost = False
command = input()


while command != 'Retire':
    tokens = command.split(' ')
    if tokens[0] == 'Fire':
        idx = int(tokens[1])
        damage = int(tokens[2])
        if 0 <= idx < len(warship):
            warship[idx] -= damage
            if warship[idx] <= 0:
                print('You won! The enemy ship has sunken.')
                lost = True
                break
    elif tokens[0] == 'Defend':
        start_idx = int(tokens[1])
        end_idx = int(tokens[2])
        damage = int(tokens[3])
        if 0 <= start_idx < len(pirate_ship) and 0 <= end_idx < len(pirate_ship):
            for idx in range(start_idx, end_idx + 1):
                pirate_ship[idx] -= damage
                if pirate_ship[idx] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    lost = True
                    break
            if lost:
                break
    elif tokens[0] == 'Repair':
        idx = int(tokens[1])
        health = int(tokens[2])
        if 0 <= idx < len(pirate_ship):
            if pirate_ship[idx] + health > max_health:
                health = max_health - pirate_ship[idx]
            pirate_ship[idx] += health
    elif tokens[0] == 'Status':
        minimum = max_health * 0.2
        count = len([x for x in pirate_ship if x < minimum])
        print(f'{count} sections need repair.')

    command = input()
if not lost:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(warship)}')