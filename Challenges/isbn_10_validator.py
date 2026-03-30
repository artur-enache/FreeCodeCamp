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
    if len(stripped) != 10:
        return False
    if not pattern.match(stripped):
        return False

    sum = 0
    for index, digit in enumerate(stripped, start=1):
        if digit == 'X':
            sum += 10 * index
        else:
            sum += int(digit) * index
    return False if sum % 11 else True

print(is_valid_isbn10("0-306-40615-2"))

# I think this has a time & space complexity of O(n), because each input is iterated over only once, so both the time
# and space increase linearly, as the input grows. But there are two operations performed for each n (two "if" statements)
# in which case, it's O(2n). But this is assuming that all inputs pass the initial validation, which is false.
# So perhaps the complexity is not linear, but I can't be sure. If I refer to my notes, I need to be concerned only with
# the "worst case scenario", which would be "all inputs pass the initial validation". Therefore, it's likely O(n) as I
# initially said.