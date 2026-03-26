# Exercise 4: Word Stats Analyzer

You're given two lists: a list of words and a list of scores (one score per word). Build a program that analyzes them.

1. **`pair_words_and_scores(words, scores)`** — Use `zip()` to pair each word with its score. Return a list of tuples. If the lists have different lengths, print a message and return `None`.

2. **`filter_long_words(words)`** — Use `filter()` and a lambda to return only words longer than 5 characters.

3. **`normalize_scores(scores)`** — Use `map()` and a lambda to normalize scores to a 0–1 range (divide each by the max score in the list).

4. **`find_word(words, query)`** — Use `enumerate()` to search for a word that starts with `query` (use `str.startswith()`). Return the index and word if found, otherwise return `None`. Stop as soon as the first match is found — use `break`.

5. **`summarize(pairs)`** — Takes the list of tuples from step 1. Use a loop with an `else` clause to iterate over pairs and print each one using an f-string. If any score is negative, `break` early and print a warning. Use the `else` clause to print "All scores valid" when the loop completes normally.

6. **`get_initials(words)`** — Use list comprehension to create a list of the first letter of each word that starts with a vowel.
