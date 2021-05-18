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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def print_all_prefixes():
    print("The numbers called by people in Bangalore have codes:")
    calls_from_bangalore = []
    calls_bangalore_to_bangalore = []
    bangalore_received_calls_codes = []
    for row in calls:
        if row[0].startswith("(080)"):
            calls_from_bangalore.append(row)
            if (row[1].startswith('7') or row[1].startswith('8') or row[1].startswith('9')) and " " in row[1]:
                code = row[1][:4]
                if code not in bangalore_received_calls_codes:
                    bangalore_received_calls_codes.append(code)
            elif row[1].startswith("("):
                st = str(row[1]).find('(') + 1
                en = row[1].find(')')
                code = row[1][st:en]
                if code not in bangalore_received_calls_codes:
                    bangalore_received_calls_codes.append(code)
            elif row[1].startswith("140"):
                code = row[1][:3]
                bangalore_received_calls_codes.append(code)
            if row[1].startswith("(080)"):
                calls_bangalore_to_bangalore.append(row[1])
    bangalore_received_calls_codes.sort()
    for code in bangalore_received_calls_codes:
        print(code)
    received_len = len(calls_bangalore_to_bangalore)
    all_calls_len = len(calls_from_bangalore)
    percentage = (received_len * 100) / all_calls_len

    print(
        f"{percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


print_all_prefixes()
