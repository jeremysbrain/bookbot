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
    book_dir = "books"
    book_ext = ".txt"

    book_title = "frankenstein"
    
    #book_contents = get_book_text(f"{book_dir}/{book_title}{book_ext}")
    #book_words = count_words(book_contents)
    #print(f"{book_words} words found in the document")

    #book_frankenstein_char_count = count_characters(book_contents)
    #sorted_char_count = count_characters_sorted(book_frankenstein_char_count)
    #print(sorted_char_count)

    print_book_report(f"{book_dir}/{book_title}{book_ext}")

main()