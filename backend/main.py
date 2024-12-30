#main.py

from fastapi import FastAPI
from core.config import settings




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