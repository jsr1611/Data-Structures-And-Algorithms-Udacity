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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def getTextRecord(index):
    msg = "First record of texts, {0} texts {1} at time {2}".format(texts[index][0], texts[index][1], texts[index][-1])
    return msg


def getCallRecord(index):
    msg = "Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(calls[index][0],
                                                                                        calls[index][1],
                                                                                        calls[index][2],
                                                                                        calls[index][-1])
    return msg


print(getTextRecord(0))
print(getCallRecord(-1))
