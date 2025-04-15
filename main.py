from stats import word_count, count_characters, sort_characters
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)
    num_words = word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")


main()