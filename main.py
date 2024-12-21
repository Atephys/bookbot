def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sorted_list = get_sorted_list(char_count)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the dictionary")
    print("")

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        else:
            print(f"The '{item['char']}' character was found {item['val']} times")

    print("--- End report ---")

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def get_word_count(text):
    word_list = text.split()
    return len(word_list)

def get_char_count(text):
    lowercase_text = text.lower()
    char_count = {}
    for char in lowercase_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(d):
    return d["val"]

def get_sorted_list(dictionary):
    sorted_list = []
    for key in dictionary:
        sorted_list.append({"char": key, "val": dictionary[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
