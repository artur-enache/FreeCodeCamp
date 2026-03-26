full_dot = '●'
empty_dot = '○'


def create_character(name, strength, intelligence, charisma):
    argument_sum = 0
    str_string = ''
    int_string = ''
    cha_string = ''

    validations = [
        (name, str, "The character name should be a string"),
        (strength, int, "All stats should be integers"),
        (intelligence, int, "All stats should be integers"),
        (charisma, int, "All stats should be integers")
    ]

    boundaries = [
        (strength, 1, 4),
        (intelligence, 1, 4),
        (charisma, 1, 4)
    ]

    for argument, data_type, error_message in validations:
        if not isinstance(argument, data_type):
            return error_message

    for argument, minimum, maximum in boundaries:
        if argument < minimum:
            return "All stats should be no less than 1"

        if argument > maximum:
            return "All stats should be no more than 4"

        argument_sum += argument

    if argument_sum != 7:
        return "The character should start with 7 points"

    if not name:
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"

    if ' ' in name:
        return "The character name should not contain spaces"

    str_string += full_dot * strength
    str_string += empty_dot * (10 - strength)

    int_string += full_dot * intelligence
    int_string += empty_dot * (10 - intelligence)

    cha_string += full_dot * charisma
    cha_string += empty_dot * (10 - charisma)

    return f"{name}\n{str_string}\n{int_string}\n{cha_string}"