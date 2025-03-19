import sys

from stats import count_words
from stats import count_characters
from stats import count_characters_sorted

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_book_report(book_file):
    book_contents = get_book_text(book_file)
    book_word_count = count_words(book_contents)
    book_sorted_char_count = count_characters_sorted(count_characters(book_contents))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for char in book_sorted_char_count:
        character = char["character"]
        count = char["count"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    print_book_report(book_path)

main()