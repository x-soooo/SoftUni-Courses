days = int(input())
daily_plunder = int(input())
expected = int(input())
days_counter = 0
total_plunder = 0
percentage = 0

for day in range(days):
    days_counter += 1
    total_plunder += daily_plunder
    if days_counter % 3 == 0:
        extra_plunder = daily_plunder * 0.5
        total_plunder += extra_plunder
    if days_counter % 5 == 0:
        total_plunder = total_plunder * 0.7

percentage = (total_plunder / expected) * 100

if total_plunder >= expected:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {percentage:.2f}% of the plunder.")




# The days are 5, and the daily plunder is 40. On the third day, the total
# plunder is 120, and since it is a third day, they gain an additional 50%
# from the daily plunder, which adds up to 140. On the fifth day, the plunder is 220, but
# they battle with a warship and lose 30% of the collected cargo, and the total becomes 154. That is more than expected.
