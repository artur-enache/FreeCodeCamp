"""String Math - https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-16"""
import pytest, re

def do_math(input_string: str) -> int:
    trim_pattern = re.compile(r'\d+.+\d+')
    trimmed_string = re.search(trim_pattern, input_string).group()

    digit_pattern = re.compile(r'\d+')
    digits = re.findall(digit_pattern, trimmed_string)

    nondigit_pattern = re.compile(r'\D+')
    nondigits = re.findall(nondigit_pattern, trimmed_string)

    result = int(digits[0])

    for index, group in enumerate(nondigits):
        if len(group) % 2 == 0:
            addition = True
        else:
            addition = False

        if addition:
            result += int(digits[index + 1])
        else:
            result -= int(digits[index + 1])

    return result

def test_1():
    assert do_math('3ab10c8') == 5

def test_2():
    assert do_math('6MINUS4') == 2

def test_3():
    assert do_math('9plus3') == 12

def test_4():
    assert do_math('5fkwo#10i#%.<>15P=@20!#B/25') == 15

def test_5():
    assert do_math('a.67,1$lk6ldf34@#LD@]2d32d2\'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt') == 67