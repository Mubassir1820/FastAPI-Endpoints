#main.py

from fastapi import FastAPI
from core.config import settings
from fastapi.responses import JSONResponse
from fastapi import status
from pydantic import BaseModel
from typing import Optional


class BookCreate(BaseModel):
    title: str
    author: str
    year: int




books = [
    {'id': 1, 'title': 'The Pragmatic Programmer', 'author': 'Andrew Hunt and David Thomas', 'year': 1999},
    {'id': 2, 'title': 'Clean Code', 'author': 'Robert C. Martin', 'year': 2008},
    {'id': 3, 'title': 'Design Patterns', 'author': 'Erich Gamma', 'year': 1994},
    {'id': 4, 'title': 'Refactoring', 'author': 'Martin Fowler', 'year': 1999},
]

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

@app.get("/books")
def get_all_books():
    return books


@app.get("/books/{book_id}")
def get_single_book(book_id: int):
    
    for book in books:
        if book['id'] == book_id:
            return book

    return JSONResponse(content={"Error!":"Book is not available!"}, status_code=status.HTTP_404_NOT_FOUND)


@app.post("/books")
def create_books(book: BookCreate):
    new_book = {
        'id': len(books)+1,
        'title': book.title,
        'author': book.author,
        'year': book.year
    }

    books.append(new_book)

    return JSONResponse(content={"Success": "Book added successfully"},status_code=status.HTTP_201_CREATED)