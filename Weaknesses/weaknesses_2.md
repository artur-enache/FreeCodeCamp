# Weaknesses Identified — Creature Arena Exercise

## 1. Short-circuit evaluation with `and`/`or` in validation

Used `and` to combine two validation checks (`not isinstance(...)` and `not 0 < len(...) <= 255`), meaning the exception only triggers when both fail simultaneously. An empty string passes the `isinstance` check, so the first condition is `False`, and short-circuiting skips the second — the invalid input gets through. This mistake was made twice across iterations. The fix required `or` so that failing either check is enough.

## 2. Inconsistent handling of the same data across related code paths

Two manifestations of the same root cause: not ensuring that related methods treat shared data identically. First, `learn_ability` stored attributes with `.title()` but checked for conflicts using the raw (unnormalized) name, while `use_ability` and `forget_ability` also applied `.title()` — so the key used to store, check, and retrieve could all differ, causing missed duplicate detection and phantom "not found" results. Second, `hasattr(self, ability_name)` caught both "ability already learned" and "name collides with a core attribute" but only reported the first case, so the user sees "ability already exists" when the real problem is a core attribute conflict. The fix: all methods operating on the same data must normalize the key the same way, and distinct error conditions sharing the same check need distinct handling.

## 3. Using a shortcut (`len()`) instead of comparing individual values for equality

Implemented `__eq__` by comparing `len(self) == len(opponent)`, which sums all stats. Two creatures with different individual stats can have the same sum (e.g. 10+5+3 vs 8+5+5 = 18). Equality requires comparing each stat individually, not an aggregate.

## 5. Filtering by value instead of by key

`list_abilities` used `getattr(self, item) not in self.core_stats` to exclude core attributes — comparing attribute values against the list. If an ability's description happened to match a core stat's value (e.g. description `"a"` matching the creature's name), it would be incorrectly filtered out. The filter should operate on attribute names (keys), not their values.

## 6. Circular reference from appending a list to itself

Appended `core_stats` to `self.core_stats` after assignment, creating a list that contains a reference to itself (`['a', 10, 1, 8, [...]]`). This happened to make the filtering "work" as a side effect, but produces an infinitely nested structure that could break iteration or deep comparison.

## 7. Exception hierarchy ordering in `except` clauses

Placed `except AppException` before `except CreatureMissing` (which inherits from `AppException`), making the child handler unreachable — the parent clause catches all subclass exceptions first. More specific exception types must come before more general ones.

## 8. Printing instead of returning — RECURRING

`roster_summary` initially printed its output instead of returning a string, and `battle` printed who lost but didn't return the winning creature. This happened in two separate methods, suggesting a pattern of conflating "produce output for the caller" with "display something to the screen."

**Recurred in:** Budget App (`second_certification_exercise.py`) — left active `print()` debug statements inside `create_spend_chart()`, a function that returns a string. Same pattern: mixing "display to screen" into a function whose job is to produce a return value.

## 9. F-string format specifiers for alignment and number formatting

Used manual padding math (computing lengths, multiplying `' '` by the difference) instead of using f-string format specifiers, which handle alignment and width directly:

```python
# Left-align in 23 chars, right-align in 7 chars
f'{description:<23}{amount:>7}'

# Format a number to 2 decimal places
f"{amount:.2f}"        # 100 -> "100.00"

# Combined: format then truncate
f"{amount:.2f}"[:7]
```

Key syntax: the format spec goes **inside** the braces after a colon — `{value:spec}`, not `{value}:spec`.
