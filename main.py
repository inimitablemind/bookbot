# Import all the necessary functions from the stats.py module.
# This allows us to use functions defined in another file.
import sys
from stats import get_book_report


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    get_book_report(book_path)


# Call the main function to start the program.
main()
