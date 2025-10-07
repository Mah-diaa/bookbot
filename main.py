import sys
from stats import get_book_text, count_words, count_letters, print_report


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)

    count = count_words(text)

    print(f"Found {count} total words")

    letter_dict = count_letters(text)

    print(letter_dict)

    print_report(count, letter_dict, book_path)


main()
