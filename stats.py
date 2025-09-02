def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_character_counts(char_counts):
    # Only include lowercase alphabetical characters
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha() and char.islower():
            char_list.append({"char": char, "num": count})
    char_list.sort(key=lambda d: d["num"], reverse=True)
    return char_list