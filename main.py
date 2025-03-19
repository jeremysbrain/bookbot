from stats import count_words
from stats import count_characters
from stats import count_characters_sorted

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_frankenstein_contents = get_book_text("books/frankenstein.txt")
    book_frankenstein_words = count_words(book_frankenstein_contents)
    print(f"{book_frankenstein_words} words found in the document")

    book_frankenstein_char_count = count_characters(book_frankenstein_contents)
    sorted_char_count = count_characters_sorted(book_frankenstein_char_count)
    print(sorted_char_count)

main()