# Write a program to read a sequence of integers and
# find and print the top 5 numbers greater than the average
# value in the sequence, sorted in descending order.

# Read from the console a single line holding space-separated integers.
# Print the above-described numbers on a single line, space-separated.
# If less than 5 numbers hold the property mentioned above, print less than 5 numbers

# All input numbers are integers in the range [-1 000 000 … 1 000 000
# The count of numbers is in the range [1…10 000].

# input 10 20 30 40 50 output 50 40


sequence_string = input()

sequence = [int(i) for i in sequence_string.split(' ')]
average_value = sum(sequence) / len(sequence)
greatest_reverse_sorted = sorted([i for i in sequence if i > average_value], reverse=True)

result = None
if greatest_reverse_sorted:
    result = ' '.join(map(str, greatest_reverse_sorted[:5]))
else:
    result = "No"

print(result)
