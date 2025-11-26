from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as arquivo:
        texto=arquivo.read()
    return texto

def main():
    try:
        print("Usage: python3 main.py <path_to_book>")
        texto=get_book_text(sys.argv[1])
        num_words=get_num_words(texto)
        num_char=get_num_char(texto)

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        sort_dict(num_char)
        print("============= END ===============")
        
    except:
        sys.exit(1)

main()
