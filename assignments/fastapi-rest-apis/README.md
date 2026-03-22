# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern, production-ready REST APIs using the FastAPI framework. You'll create an API that handles HTTP requests, manages data, and returns JSON responses while exploring key concepts like routing, request validation, and error handling.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application with Basic Routing

#### Description
Create a FastAPI application with fundamental routing to handle GET and POST requests. Set up the project structure and establish endpoints that respond to client requests.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn for running the server
- Create a main FastAPI application instance
- Implement at least 3 GET endpoints with different routes
- Implement at least 1 POST endpoint that accepts request data
- Run the server successfully and respond to requests

### 🛠️ Implement Data Models and Request Validation

#### Description
Define Pydantic models for request and response data to ensure type safety and automatic validation. Create endpoints that use these models to validate incoming data.

#### Requirements
Completed program should:

- Define Pydantic models for your API data structures
- Use models in request bodies to validate incoming data
- Provide meaningful error messages for invalid requests
- Document model fields with descriptions
- Return properly structured JSON responses

### 🛠️ Add Error Handling and Status Codes

#### Description
Implement proper HTTP error handling and status codes to make your API more robust and informative for clients.

#### Requirements
Completed program should:

- Return appropriate HTTP status codes (200, 201, 400, 404, etc.)
- Handle common errors gracefully with custom error responses
- Raise HTTPException for validation and not-found errors
- Include error details in response messages
- Test error scenarios manually or with provided test cases
