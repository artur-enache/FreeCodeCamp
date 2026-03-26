# words = []; scores = []

def pair_words_and_scores(words, scores):
    if len(words) != len(scores):
        print("Words and scores do not match")
        return None

    return list(zip(words, scores))

def filter_long_words(words):
    return list(filter(lambda x: len(x) > 5, words))

def normalize_scores(scores):
    return list(map(lambda x: x / max(scores), scores))

def find_word(words, query):
    to_return = None
    for index, word in enumerate(words):
        if word.lower().startswith(query.lower()):
            to_return = (index, word)
            break
    else:
        return None

    return to_return

def summarize(pairs):
    for pair in pairs:
        print(f"Word: {pair[0]}, Score: {pair[1]}")
        if pair[1] < 0:
            print("Warning: score is negative")
            break
    else:
        print("All scores are valid")

def get_initials(words):
    return [ word[0] for word in words if word.lower().startswith(('a', 'e', 'i', 'o', 'u', 'y')) ]