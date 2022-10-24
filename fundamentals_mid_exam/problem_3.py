rating = [int(i) for i in input().split(', ')]
entry = int(input())
value = rating[entry]
left = rating[:entry]
right = rating[entry + 1:]
value_left = 0
value_right = 0
sum_left = 0
sum_right = 0

command = input()
if command == 'cheap':
    for i in left:
        if value > i:
            value_left = i
    for r in right:
        if value > r:
            value_right = r
    if value_left == value_right:
        print(f"Left - {value_left}")
    elif value_left > value_right:
        print(f"Left - {value_left}")
    elif value_right > value_left:
        print(f"Right - {value_right}")

elif command == 'expensive':
    sum_left = sum(left)
    sum_right = sum(right)
    if sum_left == sum_right:
        print(f"Left - {sum_left}")
    else:
        if sum_left > entry:
            print(f"Left - {sum_left}")
        elif sum_right > entry:
            print(f"Right - {sum_right}")





