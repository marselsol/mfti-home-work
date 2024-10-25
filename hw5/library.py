from typing import List, Optional

from exceptions import BookNotAvailable
from models import Book, User

books: List[Book] = []
users: List[User] = []


def add_book(book: Book) -> None:
    books.append(book)


def find_book(title: str) -> Optional[Book]:
    for book in books:
        if book.title == title:
            return book
    return None


def is_book_borrow(title: str) -> bool:
    book = find_book(title)
    if book and book.available:
        return False
    raise BookNotAvailable(f"The book '{title}' is not available")


def log_operation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Operation {func.__name__} was performed with args: {args}, kwargs: {kwargs}")
        return result

    return wrapper


def return_book(title: str) -> None:
    book = find_book(title)
    if book:
        book.available = True
