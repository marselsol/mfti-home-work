from typing import List

from pydantic import BaseModel, EmailStr


class Book(BaseModel):
    title: str
    author: str
    year: int
    available: bool
    categories: List[str] = []


class User(BaseModel):
    name: str
    email: EmailStr
    membership_id: str


class Library(BaseModel):
    books: List[Book]
    users: List[User]

    def total_books(self) -> int:
        return len(self.books)
