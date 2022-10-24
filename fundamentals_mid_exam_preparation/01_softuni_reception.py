e1 = int(input())
e2 = int(input())
e3 = int(input())
students = int(input())

answer_hour = e1 + e2 + e3
time = 0

while students > 0:
    students -= answer_hour
    time += 1
    if time % 4 == 0:
        time += 1

print(f"Time needed: {time}h.")