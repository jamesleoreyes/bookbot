import sys
from stats import get_word_count, get_character_count, get_sorted_dict

def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()


def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {sys.argv[1]}...')
    print('----------- Word Count ----------')
    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count((book_text))
    print(f"Found {word_count} total words")
    char_counts = get_character_count(book_text)
    print('--------- Character Count -------')
    sorted_chars = get_sorted_dict((char_counts))
    
    for entry in sorted_chars:
        if not entry['char'].isalpha():
            continue
        print(f"{entry['char']}: {entry['num']}")
    
main()