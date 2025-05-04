from stats import get_num_words
from stats import get_char_count
import sys

def main():
    if len(sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
    try:
        file_path = sys.argv[1]
        content = get_num_words(file_path)
        char_lists = get_char_count(file_path)

        if len(sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        

        print("============ BOOKBOT ============")
        print(f"Analizing book found at {file_path}")
        print("----------- Word Count ----------")
        print(f"Found {content} total words")
        print("--------- Character Count -------")
        for char_dict in char_lists:
            if char_dict["char"].isalpha():
                print(f"{char_dict['char']}: {char_dict['num']}")
        print("============= END ===============")

    except Exception as e:
        print(f"error: {e}")
main()