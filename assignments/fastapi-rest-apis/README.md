# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice defining endpoints, validating request data, and handling CRUD operations. You will create an in-memory book catalog and explore its interactive API documentation.

## 📝 Tasks

### 🛠️ Create the Book Catalog and Read Endpoints

#### Description
Create a FastAPI application for a book catalog. Store books in an in-memory collection, with each book containing an integer `id`, a `title`, an `author`, and a `year`.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn, and create an application that can be run locally with Uvicorn.
- Implement `GET /books` to return all books as JSON.
- Implement `GET /books/{book_id}` to return one book, or a `404` response when the ID is not found.
- Include at least two sample books in the in-memory collection.


### 🛠️ Add Books with Validated Requests

#### Description
Add an endpoint that accepts a JSON request to create a book. Use a Pydantic model to validate the request body before adding the book to the collection.

#### Requirements
Completed program should:

- Define a request model with `title`, `author`, and `year` fields.
- Reject requests with a missing or blank title or author, or a year outside the range 1–2100.
- Implement `POST /books` to assign a unique integer ID, store the new book, and return it with status code `201`.
- Confirm valid and invalid requests using the interactive documentation at `/docs`.


### 🛠️ Complete the Book CRUD API

#### Description
Extend the catalog so clients can update and remove books. Keep using the in-memory collection and return clear HTTP responses for missing IDs.

#### Requirements
Completed program should:

- Implement `PUT /books/{book_id}` to replace a book's details and return the updated book.
- Implement `DELETE /books/{book_id}` to remove a book and return a successful response.
- Return `404` for update or delete requests that use an ID that does not exist.
- Verify that create, read, update, and delete operations work using `/docs` or automated API tests.
