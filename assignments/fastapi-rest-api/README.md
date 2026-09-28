# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for a book catalog using FastAPI. You will create endpoints, validate request data, return appropriate HTTP status codes, and test the API with FastAPI's interactive documentation.

## 📝 Tasks

### 🛠️ Start the FastAPI Application

#### Description
Install FastAPI and Uvicorn, complete the root endpoint in `starter-code.py`, and run the development server with `uvicorn starter-code:app --reload`.

#### Requirements
Completed program should:

- Install the required packages with `python -m pip install fastapi uvicorn`
- Return `{"message": "Welcome to the Book Catalog API"}` from `GET /`
- Be accessible at `http://127.0.0.1:8000`
- Display interactive API documentation at `http://127.0.0.1:8000/docs`


### 🛠️ Read Books from the Catalog

#### Description
Create endpoints that return all books or one book selected by its numeric ID. Use an HTTP error when a requested book does not exist.

#### Requirements
Completed program should:

- Return the complete catalog from `GET /books`
- Return the matching book from `GET /books/{book_id}`
- Return status code `404` with the detail `Book not found` for an unknown ID
- Use FastAPI's `HTTPException` for the not-found response


### 🛠️ Add a Validated Book

#### Description
Create a request model and an endpoint that adds a book to the in-memory catalog. Let FastAPI validate the submitted JSON data.

#### Requirements
Completed program should:

- Define a Pydantic model with `title`, `author`, and `year` fields
- Require non-empty text for both `title` and `author`
- Accept publication years from 1450 through 2100
- Add a book with `POST /books` and assign it a unique numeric ID
- Return the created book with status code `201`


### 🛠️ Update and Delete Books

#### Description
Finish the catalog's CRUD operations by creating endpoints that update and delete existing books. Test successful and unsuccessful requests in the interactive documentation.

#### Requirements
Completed program should:

- Replace an existing book's data with `PUT /books/{book_id}`
- Remove an existing book with `DELETE /books/{book_id}`
- Return the updated book after a successful update
- Return status code `204` with no response body after a successful deletion
- Return status code `404` with the detail `Book not found` when either endpoint receives an unknown ID
