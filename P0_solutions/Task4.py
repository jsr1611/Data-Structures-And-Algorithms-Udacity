"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def add_numbers(dataset):
    for row in dataset:
        possible_telemarketer.add(row[0])
        other_numbers.add(row[1])


def remove_numbers(dataset):
    for row in dataset:
        possible_telemarketer.discard(row[0])
        possible_telemarketer.discard(row[1])


possible_telemarketer = set()
other_numbers = set()
add_numbers(calls)
possible_telemarketer = possible_telemarketer.difference(other_numbers)
remove_numbers(texts)
numbers = list(possible_telemarketer)
numbers.sort()
print("These numbers could be telemarketers: ")
for num in numbers:
    print(num)
