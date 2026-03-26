# Weaknesses Identified — User Config Manager Exercise

## 1. Falsy values for empty-check

**What happened:** Used `len(settings.keys()) == 0` instead of `not settings`.

**What I already knew:** Empty values are falsy (`python_notes.md:166`). This extends to empty collections (`{}`, `[]`, `()`), so `not settings` is the idiomatic way to check if a dictionary is empty.

## 2. List comprehension + `join()` — RECURRING

**What happened:** Built a string with a loop and `+=` concatenation in `view_settings`:
```python
output = 'Current User Settings:\n'
for key, value in settings.items():
    output += f'{key.capitalize()}: {value}\n'
```

**What I already knew:** List comprehensions (`python_notes.md:110-121`) and practiced them in `exercise_4.py` (`get_initials`, `filter_long_words`). Could have combined a comprehension with `'\n'.join()`:
```python
lines = '\n'.join(f'{key.capitalize()}: {value}' for key, value in settings.items())
return f'Current User Settings:\n{lines}\n'
```

**Recurred in:** Budget App (`second_certification_exercise.py`) — the `__str__` method and the vertical labels section in `create_spend_chart()` both build strings with loop + `+=` instead of using comprehension + `join()`.

## 3. `key in settings` vs `key in settings.keys()`

**What happened:** Used `key in settings.keys()` to check for key existence.

**What I already knew:** `.keys()` returns a view object (`new_python_notes.md:12-13`). The `in` operator on a dictionary already checks keys by default, so `key in settings` is simpler and equivalent.
