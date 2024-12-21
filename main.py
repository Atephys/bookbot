def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    print(book_text)

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

main()
