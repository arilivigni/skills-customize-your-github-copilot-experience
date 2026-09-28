from typing import Annotated

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field


app = FastAPI(title="Book Catalog API")


class BookCreate(BaseModel):
    title: Annotated[str, Field(min_length=1)]
    author: Annotated[str, Field(min_length=1)]
    year: Annotated[int, Field(ge=1450, le=2100)]


books = [
    {
        "id": 1,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
    },
    {
        "id": 2,
        "title": "A Wrinkle in Time",
        "author": "Madeleine L'Engle",
        "year": 1962,
    },
]


@app.get("/")
def read_root():
    pass


@app.get("/books")
def read_books():
    pass


@app.get("/books/{book_id}")
def read_book(book_id: int):
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookCreate):
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    pass
