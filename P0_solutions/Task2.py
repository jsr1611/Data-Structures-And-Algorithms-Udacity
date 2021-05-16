"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def getLongestCall():
    differentCalls = {}
    for index in range(len(calls)):
        callerNumber = calls[index][0]
        receivingNumber = calls[index][1]
        callDuration = int(calls[index][-1])

        if callerNumber in differentCalls:
            differentCalls[callerNumber] += callDuration
        else:
            differentCalls[callerNumber] = callDuration
        if receivingNumber in differentCalls:
            differentCalls[receivingNumber] += callDuration
        else:
            differentCalls[receivingNumber] = callDuration
    number = max(differentCalls, key=differentCalls.get)
    longest_call = differentCalls.get(number)

    print(f"{number} spent the longest time, {longest_call} seconds, on the phone during September 2016.")


getLongestCall()
