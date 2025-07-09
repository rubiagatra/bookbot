from stats import get_num_words, get_count_characters, sorted_list_dictionaries 
import sys

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    path = sys.argv[1]
    print(f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {get_num_words(path)} total words
--------- Character Count -------
""", end='')
    character_list = sorted_list_dictionaries(path)
    for cl in character_list:
        if cl["char"].isalpha():
            print(f"{cl["char"]}: {cl["num"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
