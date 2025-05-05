def book_word_count(book):
    words=book.split()
    length = len(words)
    return length



def letter_analyse(book):
    book = book.lower()
    chars = list(book)
    char_count = {}
    for x in chars:
        if x in char_count: 
            char_count[x] = char_count[x] + 1
        else:
            char_count[x] = 1
    return char_count

def sort_letters(letters):
    sorted_dict = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

def filtered_letters(letters):
    filtered_dict = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
    dict_list = []
    filtered_dict_list = []
    for char in filtered_dict:
        new_dict = {"char": char, "num": filtered_dict[char]}
        dict_list.append(new_dict)
    for pair in dict_list:
        #print(pair)
        if pair["char"].isalpha():
            filtered_dict_list.append(pair)
    return filtered_dict_list