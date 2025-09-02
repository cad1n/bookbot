import sys
from stats import get_book_text, count_words, count_characters, sort_character_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_chars = sort_character_counts(char_counts)
    print(f"--- Begin report of {filepath} ---")
    print(f"Found {num_words} total words")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("--- End report ---")

main()
