# pip install pydantic[email] в терминале ввести, чтобы все работало корректно

from library import add_book, is_book_borrow, return_book
from models import Book

if __name__ == "__main__":
    book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925, available=True)
    book2 = Book(title="1984", author="George Orwell", year=1949, available=False)

    add_book(book1)
    add_book(book2)

    try:
        is_book_borrow("1984")
    except Exception as e:
        print(e)

    return_book("1984")
