# Exercise 5: Log File Analyzer

You are given a log file (`server.log`) where each line follows this format:

```
YYYY-MM-DD HH:MM:SS <thread_id> LEVEL message
```

Build a program that parses and analyzes the log entries.

---

1. **`parse_line(line)`** — Takes a single log line string and returns a tuple of `(date, time, thread, level, message)`. Each field is a string. If the line is empty or malformed (fewer than 5 parts), return `None`.

2. **`parse_log(lines)`** — Takes a list of raw log lines. Use list comprehension to return a list of parsed tuples, skipping any lines where `parse_line` returns `None`.

3. **`filter_by_level(entries, level)`** — Takes the list of parsed tuples and a log level string (e.g. `"ERROR"`). Use `filter()` and a lambda to return only entries matching that level (case-insensitive).

4. **`count_by_level(entries)`** — Takes the list of parsed tuples. Returns a dictionary with each log level as a key and the number of occurrences as the value.

5. **`find_entries(entries, keyword)`** — Use `enumerate()` to search through entries. Return a list of `(index, entry)` tuples where the message contains the keyword (case-insensitive). Return an empty list if nothing is found.

6. **`top_level(entries)`** — Use `count_by_level()` and `max()` to return the log level that appears most often, as a string.

7. **`summarize(entries)`** — Prints a summary report using f-strings. Include:
   - Total number of entries
   - Count per log level
   - The most frequent log level
   - A list of all ERROR messages (just the message part)
