from math import ceil

budget = float(input())
students = int(input())
flour = float(input())
egg = float(input())
apron = float(input())

needed_items = 0
needed_apron = apron * ceil(students * 1.2)
needed_eggs = egg * 10
students_count = 0
free_packages = 0

for st in range(students + 1):
    students_count += 1
    needed_items = needed_apron + needed_eggs * students + (flour * (students - free_packages))
    if students_count % 5 == 0:
        free_packages += 1

total_money = abs(budget - needed_items)
if needed_items <= budget:
    print(f"Items purchased for {needed_items:.2f}$.")
else:
    print(f"{total_money:.2f}$ more needed.")


