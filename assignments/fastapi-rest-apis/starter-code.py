"""
FastAPI REST API Starter Code

This is a starter template for building REST APIs with FastAPI.
Complete the tasks by implementing the required endpoints and models.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# TODO: Define your Pydantic models here
# Example:
# class Item(BaseModel):
#     name: str
#     description: str
#     price: float


# Initialize FastAPI application
app = FastAPI(
    title="My REST API",
    description="A REST API built with FastAPI",
    version="1.0.0"
)


# TODO: Implement GET endpoints
# Example:
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to my API"}


# TODO: Implement POST endpoints
# Example:
# @app.post("/items/")
# def create_item(item: Item):
#     return {"item": item, "message": "Item created successfully"}


# TODO: Implement error handling
# Example:
# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     if item_id < 0:
#         raise HTTPException(status_code=400, detail="Invalid item ID")
#     return {"item_id": item_id}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
