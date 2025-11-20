from stats import sort_char, count_words
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    start_str = f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n"
    start_str += f"----------- Word Count ----------\nFound {count_words(path)} total words\n"
    dict_list = sort_char(path)
    start_str += f"--------- Character Count -------\n"

    for dic in dict_list:
        if dic["char"].isalpha():
            start_str += f"{dic["char"]}: {dic["num"]}\n"

    start_str += f"============= END ==============="

    print(start_str)


main()
