"""CHALLENGE:

Given a string, determine if it's a valid ISBN-10.

An ISBN-10 consists of hyphens ("-") and 10 other characters. After removing the hyphens ("-"):

    The first 9 characters must be digits, and
    The final character may be a digit or the letter "X", which represents the number 10.

To validate it:

    Multiply each digit (or value) by its position (multiply the first digit by 1, the second by 2, and so on).
    Add all the results together.
    If the total is divisible by 11, it's valid."""

import re

pattern = re.compile(r"^\d{9,10}[X]{0,1}$")

def is_valid_isbn10(s):
    stripped = s.replace('-', '')
    print('stripped: ', stripped)
    if not pattern.match(stripped):
        return False

    sum = 0
    for index, digit in enumerate(stripped, start=1):
        print('index, digit: ', (index, digit))
        if digit == 'X':
            sum += 10 * index
        else:
            sum += int(digit) * index
    print('sum: ', sum)
    return False if sum % 11 else True

print(is_valid_isbn10("0-306-40615-2"))