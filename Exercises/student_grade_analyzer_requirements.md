# Exercise 2: Student Grade Analyzer

Build a program that manages a list of students and analyzes their grades. Each student is a dictionary with: name (string), age (int), grades (tuple of ints), and email (string).

1. **`add_student(students, name, age, grades, email)`** — Adds a student to the list.
   - Validate all inputs using `isinstance()` before adding.
   - Check that name is non-empty, age is in a reasonable range, and grades is a tuple.
   - Use augmented assignment to track how many students have been added.

2. **`classify_student(student)`** — Uses conditionals to classify a student based on their average grade:
   - 90+: "Excellent"
   - 70–89: "Good"
   - 50–69: "Needs Improvement"
   - Below 50: "At Risk"
   - Use `if`/`elif`/`else`.

3. **`search_students(students, query)`** — Search by name using partial, case-insensitive matching (string slicing/comparison).

4. **`display_students(students, debug_mode=False)`** — Print all students using f-strings. If `debug_mode` is True, also show `type()` for each field.

5. **`should_contact_parent(student, has_email)`** — Returns whether to contact a parent. Use `and`/`or` logic:
   - Contact if the student is "At Risk" **and** `has_email` is truthy.
   - Also contact if the student is "Needs Improvement" **and** age is under 16.
   - Think about short-circuit evaluation and falsy values (what happens if email is `""`?).
