people_waiting_for_the_lift = int(input())
current_state_of_the_list = input()
current_state_of_the_list = [int(i) for i in current_state_of_the_list.split(' ')]

for wagon_index in range(len(current_state_of_the_list)):
    for person in range(people_waiting_for_the_lift):
        if current_state_of_the_list[wagon_index] < 4:
            current_state_of_the_list[wagon_index] += 1
            people_waiting_for_the_lift -= 1
        else:
            break

if people_waiting_for_the_lift == 0 and sum(current_state_of_the_list) < len(current_state_of_the_list) * 4:
    print("The lift has empty spots!")
elif people_waiting_for_the_lift > 0 and sum(current_state_of_the_list) == len(current_state_of_the_list) * 4:
    print(f"There isn't enough space! {people_waiting_for_the_lift} people in a queue!")
print(' '.join(map(str, current_state_of_the_list)))
