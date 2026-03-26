import re

file_path = "/home/arturk/Desktop/Python/FreeCodeCamp/server.log"
date_pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
time_pattern = re.compile(r"\d{2}:\d{2}:\d{2}")
thread_pattern = re.compile(r"<\d+>")
level_pattern = re.compile(r"^[A-Z]+$")
message_pattern = re.compile(r"(.|\s)*\S(.|\s)*")
validations = [date_pattern, time_pattern, thread_pattern, level_pattern, message_pattern]

def validator(line):
    try:
        date, time, thread, level, *message = line.split(' ')
        message = ' '.join(message)
    except ValueError:
        return False

    return all(pattern.match(field) for pattern, field in zip(validations, [date, time, thread, level, message]))

def parse_line(line):
    if not validator(line):
        return None
    else:
        date, time, thread, level, *message = line.split(' ')
        message = ' '.join(message)
        return date, time, thread, level, message

def parse_log(file):
    with open(file, 'r') as file_handle:
        lines = file_handle.readlines()
    to_filter = [parse_line(line) for line in lines]
    return [line for line in to_filter if line is not None]

def filter_by_level(entries, level):
    # Entries = result of parse_log()
    return filter(lambda entry: entry[3] == level, entries)

def count_by_level(entries):
    # Entries = result of parse_log()
    list_of_levels = [line[3] for line in entries]
    unique_levels = set(list_of_levels)
    dictionary_levels = {}

    # TODO: replace with a single loop over entries to avoid re-iterating the list once per unique level
    for level in unique_levels:
        dictionary_levels[level] = sum(1 for _ in filter_by_level(entries, level))

    return dictionary_levels

def find_entries(entries, keyword):
    # Entries = result of parse_log()
    # TODO: enumerate(entries) directly — the inner list comprehension is an unnecessary copy
    return [(index, entry) for (index, entry) in enumerate([line for line in entries]) \
            if keyword.lower() in entry[-1].lower()]

def top_level(entries):
    # Entries = result of parse_log()
    max_levels = count_by_level(entries)
    return max(max_levels, key=max_levels.get)
    # TODO: remove dead code
    # for key, value in max_levels.items():
    #     if value == max_value:
    #         output += f'Level: {key}, occurrences: {value}\n'

    #return output

def summarize(entries):
    # Entries = result of parse_log()
    total_entries = len(entries)
    level_count = count_by_level(entries)
    level_string = ''
    for key, value in level_count.items():
        level_string += f'{key}: {value}\n'
    most_freq = top_level(entries)
    error_items = [item[-1].rstrip() for item in filter_by_level(entries, "ERROR")]
    error_list = '\n'.join(error_items)
    output = (f'Total number of entries: {total_entries}\n'
              f'-----------------------------------------\n'
              f'Count per log level:\n'
              f'{level_string}\n'
              f'-----------------------------------------\n'
              f'Most frequent log level: {most_freq}\n'
              f'-----------------------------------------\n'
              f'All error messages:\n'
              f'{error_list}')
    return output

# TODO - if the error message contains a stack, get only the first line of the stack
# maybe also try to make it work with multiple log files? Ex: parse HA log, and when it finds an error at HH:MM:SS.mmm
# then crossref it with specific log files; if the error is related to identity > cross ref with identity log but only at
# HH:MM:SS (less precision) and output the result
# Or think about a way it would be useful