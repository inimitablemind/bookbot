def get_book_text(book):
    with open(book) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_character_count(text):
    char_count = {}
    for char in text:
        char = char.lower()  # Normalize to lowercase
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count


def sort_on(char_count):
    return char_count["count"]


def sort_char_count(char_count):
    sorted_char_list = []
    for letter in char_count:
        temp = {"letter": letter, "count": char_count[letter]}
        sorted_char_list.append(temp)
    sorted_char_list.sort(key=sort_on, reverse=True)
    return sorted_char_list
