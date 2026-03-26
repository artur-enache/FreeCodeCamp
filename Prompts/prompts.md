# Claude Prompts

A collection of prompts used for Python study assistance.

---

## Note Taking

I will be studying Python and taking notes. I will be sending the notes in this session, and you don't need to do anything with them yet. Once I am done studying, I will ask you to gather the notes and save them in a markdown file: `~/Desktop/Python/FreeCodeCamp/Notes/new_notes.md`.

Before organizing, read the existing file at `~/Desktop/Python/FreeCodeCamp/Notes/python_notes.md`. Use its section order as the reference for logical topic ordering. Place each note under its appropriate section, following that same order. If a note belongs to a section that doesn't exist yet, insert the new section at a position that fits logically within the existing order — do not append everything to the end. You must not change any of the text I have written.

---

## Note Consolidation

There are two files: `~/Desktop/Python/FreeCodeCamp/Notes/new_notes.md` and `~/Desktop/Python/FreeCodeCamp/Notes/python_notes.md`. Read `python_notes.md` in order to understand the structure, then consolidate the `new_notes.md` file into the `python_notes.md` file, and respect the logical topic ordering. Place each note under its appropriate section, following that same order. If a note belongs to a section that doesn't exist yet, insert the new section at a position that fits logically within the existing order — do not append everything to the end. You must not change any of the text I have written.

---

## Exercise Script Generator

The directory `~/Desktop/Python/FreeCodeCamp` contains the following subdirectories:

- `./Notes` — with the files `new_notes.md` and `python_notes.md`: notes I took while studying Python. `new_notes.md` contains the most recent notes, that I haven't practiced much.
- `./Exercises` — with exercise requirements & scripts that I wrote; all the exercise requirements have covered contents from `python_notes.md`, to help me assimilate that information better.
- `./Weaknesses` — with a file containing some of the weaknesses I have in Python. These weaknesses have been identified by analyzing the Python scripts I wrote (in `./Exercises`) and seeing which tasks I solved without using knowledge that was already a part of my notes (hence, I should have known to use them while fulfilling the exercise).

Your task is to devise an exercise that I find interesting (the resulting script has some practical value, or it is an entertaining toy). The task execution has two stages:

1. Analyse the files under `./Exercises`, `./Notes` and `./Weaknesses`, and determine which topics I have not practiced lately (use the file's `ctime` to aid here), and where my weaknesses are.
2. Devise an exercise that satisfies the task as I described it. Do not give away information about how specifically I should implement the scripts (the files under `./Exercises/*_requirement.md` are a good model).

---

## Weakness Analysis

Your new task is the following:

- `~/Desktop/Python/FreeCodeCamp/Notes` — this contains most of my knowledge about Python
- `~/Desktop/Python/FreeCodeCamp/Weaknesses` — this contains weaknesses in my knowledge of Python

Using the two resources above, I want you to examine the script I wrote, and find out:

- Which of the Python knowledge I have & I should have used, but didn't
- Which big mistakes I have made in the script
- Which of my existing weaknesses are present in this script

---

## Exercise Quiz Generator

I am learning & practicing Python. The following files represent the extent of my knowledge:

| File | Purpose |
|------|---------|
| `~/Desktop/Python/FreeCodeCamp/Notes/new_notes.md` | Topics I learned recently but practiced very little. Treat everything here as unpracticed. |
| `~/Desktop/Python/FreeCodeCamp/Notes/python_notes.md` | Topics I have practiced (maps to the 10% "already practiced" category). |
| `~/Desktop/Python/FreeCodeCamp/Exercises/*.py` | Exercises I completed so far. |
| `~/Desktop/Python/FreeCodeCamp/Weaknesses/*.md` | Common mistakes and knowledge gaps, extracted from my exercises. |

**Task:** Create a single HTML file containing 50 targeted Python exercises. Use Pyodide (loaded from CDN) to run Python entirely in the browser — no server, no installation.

### Exercise Distribution (out of 50)

| Category | Count | Source |
|----------|-------|--------|
| Unpracticed topics | ~30 (60%) | `new_notes.md` |
| Weakness targeting | ~15 (30%) | `Weaknesses/` directory |
| Reinforcement | ~5 (10%) | `python_notes.md` |

### Exercise Design

- Exercises must be tightly focused on one concept each. If the exercise is about list comprehension, it should test list comprehension — not classes, docstrings, polymorphism, or anything unrelated.
- The goal is to solidify existing knowledge, not introduce new concepts. Difficulty should match my current level.
- Most exercises should be "write a function/expression" style (simplest to verify). Include a few (~5–8) in other formats: predict the output, fix a bug, or fill in the blanks.

### Page Layout

- Numbered exercise descriptions
- Below each description, a text box for typing my solution
- Below each text box, a **Verify** button and a **Reset** button
- **Verify** runs a Python test against my solution. If wrong, turn the text box border red and show a generic error message (no hints, no expected output).
- **Reset** clears the text box and resets the test result so I can retry.
- Keep the layout simple — one scrollable page is fine.

### Persistent Storage

- Use `localStorage` to persist all textarea contents and solved/unsolved state across page refreshes and browser restarts.
- Save textarea content on every keystroke. Restore it on page load.
- Save solved state when Verify succeeds. Clear it when Verify fails.
- Reset must clear both the textarea content and solved state from `localStorage`.

### Process

Plan this task before executing it. After generating the output, test it, fix any errors, and test again. Repeat until the output works correctly before providing the final result.