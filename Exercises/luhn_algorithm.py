import pytest

def verify_card_number(digits: str) -> str:
    sanitize = ' -'

    for char in sanitize:
        digits = digits.replace(char, '')

    digits_to_list = [ int(elem) for elem in digits ]
    length = len(digits_to_list)

    # Step backwards from the second to last element, and double every other digit
    for i in range(-2, -length - 1, -2):
        doubled = digits_to_list[i] * 2
        digits_to_list[i] = (doubled - 9) if doubled > 9 else doubled

    if sum(digits_to_list) % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'

def test_1():
    assert verify_card_number('453914889') == 'VALID!'

def test_2():
    assert verify_card_number('4111-1111-1111-1111') == 'VALID!'

def test_3():
    assert verify_card_number('453914881') == 'INVALID!'

def test_4():
    assert verify_card_number('1234 5678 9012 3456') == 'INVALID!'