def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    word_count = get_word_count(book_text)
    print(word_count)

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def get_word_count(text):
    word_list = text.split()
    return len(word_list)

main()
