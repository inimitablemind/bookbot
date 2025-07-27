def get_book_text(path):
    """
    Opens and reads the content of a book file.

    Args:
        path (str): The file path to the book.

    Returns:
        str: The entire content of the book as a single string.
    """
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(text):
    """Counts the total number of words in a given text."""
    num_words = len(text.split())
    return num_words


def get_char_counts(text):
    """
    Counts the occurrences of each character in the text.

    Note: This function iterates through the text twice, which is inefficient.
    A more optimal approach would be to use `dict.get(char, 0) + 1` in a single loop.
    """
    char_counts = {}
    lowered_text = text.lower()
    # First loop: Initializes all unique characters found in the lowered_text with a count of 0.
    for char in lowered_text:
        char_counts[char] = 0
    # Second loop: Increments the count for each character.
    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
    return char_counts


def get_char_report(char_counts):
    """Converts a character counts dictionary to a list of dictionaries, filtering for alphabetic characters."""
    char_report_list = []
    for char in char_counts:
        if char.isalpha():
            char_report_list.append({"char": char, "count": char_counts[char]})
    return char_report_list


def sort_by_count(item):
    """
    A helper function for sorting.

    This function is intended to be used as the `key` argument in a sort operation.
    It tells the sort method to use the value of the 'count' key from a dictionary
    as the basis for sorting.
    """
    return item["count"]


def get_book_report(book_path):
    """
    The main function that orchestrates the book analysis and report generation.
    """
    # Define the path to the book file.
    # This path is expected to be passed as a command line argument.
    # Read the book's text into a variable.
    book_text = get_book_text(book_path)
    # Calculate the total number of words in the text.
    num_words = get_num_words(book_text)
    # Get a dictionary of character counts from the text.
    char_counts = get_char_counts(book_text)
    # Convert the character count dictionary into a list of dictionaries.
    # This format is more suitable for sorting and reporting.
    char_report = get_char_report(char_counts)
    # Sort the list of characters in descending order based on their count.
    # The `get_count_from_report_item` function is used as the key to specify that sorting
    # should be based on the 'count' value in each dictionary.
    char_report.sort(reverse=True, key=sort_by_count)

    # Print the final, formatted report to the console.
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # Loop through the sorted list and print each character's count.
    for item in char_report:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")
