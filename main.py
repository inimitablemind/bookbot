import sys
from stats import get_num_words, get_book_text, get_character_count, sort_char_count


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_count = get_character_count(book_text)
    sorted_char_list = sort_char_count(char_count)
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in sorted_char_list:
        print(f"{letter['letter']}: {letter['count']}")
    print("============= END ===============")


main()
