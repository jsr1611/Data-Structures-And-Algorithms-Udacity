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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

result = set()


def allDifferentRecords(dataset):
    for row in dataset:
        result.add(row[0])
        result.add(row[1])
    return len(result)


allDifferentRecords(calls)
allDifferentRecords(texts)
print(f"There are {len(result)} different telephone numbers in the records.")
