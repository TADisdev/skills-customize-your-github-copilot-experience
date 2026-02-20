# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to practice route creation, request handling, and API response design in Python.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Set up a FastAPI project and implement endpoints for a simple resource (for example, tasks or books) that supports creating and retrieving data.

#### Requirements
Completed program should:

- Create a FastAPI app instance and run successfully.
- Implement a `GET` endpoint that returns all items.
- Implement a `POST` endpoint that adds a new item.
- Return JSON responses for both endpoints.


### 🛠️	Add Validation and Error Handling

#### Description
Improve the API by validating request data and handling common errors so responses are clear and predictable.

#### Requirements
Completed program should:

- Use Pydantic models to validate incoming request data.
- Return a clear error response when invalid data is sent.
- Return an appropriate response when an item is not found.
- Keep data in memory using a list or dictionary for this assignment.
