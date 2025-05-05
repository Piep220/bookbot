from stats import book_word_count, letter_analyse, sort_letters, filtered_letters
import sys

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book = args[1]
    #book = "books/frankenstein.txt"
    book_text = get_book_text(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count(book_text)} total words")
    print("--------- Character Count -------")
    letters = letter_analyse(book_text)
    #print(letters)
    #print(sort_letters(letters))
    print_dict_list(filtered_letters(letters))
    print("============= END ===============")
    return 

def print_dict_list(list):
    for pair in list:
        print(f"{pair["char"]}: {pair["num"]}")

def get_book_text(book_loc):
    with open(book_loc) as f:
        file_contents = f.read()
    return file_contents


main()