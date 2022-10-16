# Author: Hussain Al Zerjawi
# Purpose: Practice the FastAPI library
# Date: 16/10/2022

from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    item.name = item.name.capitalize()
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

# A database to test the methods with
food_items_db = [{"item_name": "Chicken"}, {
    "item_name": "Beef"}, {"item_name": "Fish"}]

# Class for predefined path parameters


class ModelName(str, Enum):
    manager = "Manager"
    developer = "Developer"
    support = "Support"

# In case my path parameter contains a path


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    # Example URL query: "http://127.0.0.1:8000/files//assets/bread.txt"
    return {"file_path": file_path}

# The GET request method for the predefined path parameters


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    # Example URL query: "http://127.0.0.1:8000/models/Developer"
    if model_name is ModelName.developer:
        return {"model_name": model_name, "message": f"{model_name} get ready to code"}
    if model_name.value == "Manager":
        return {"model_name": model_name, "message": "Be a good Manager"}
    return {"model_name": model_name, "message": "Support me!"}


@app.get("/items/me")
async def read_user_me():
    # Example URL query: "http://127.0.0.1:8000/items/me"
    return {"user_id": "I am the current user"}

# Request Method with an optional parameter of q
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        # Example URL query: "http://127.0.0.1:8000/items/1?q=king"
        item.update({"q": q})
    if not short:
        # Example URL query: "http://127.0.0.1:8000/items/100?q=tower?short=true"
        item.update({"description": "This is an item that has a long description"})
    # Example URL query: "http://127.0.0.1:8000/items/100"
    return item

# Request method to handle "query" parameters

# Query Parameter
# When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

@app.get("/items/")
# skip and limit have default values in case they are not defined within the URL query
async def read_item(skip: int = 0, limit: int = 10):
    # Example URL query: "http://127.0.0.1:8000/items/" for default values or "http://127.0.0.1:8000/items/?skip=1&limit=3"
    return food_items_db[skip: skip + limit]


# Multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    # Example URL query: "http://127.0.0.1:8000/users/24/items/sugar"
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        # Example URL query: "http://127.0.0.1:8000/users/24/items/sugar?q=I+am+king&short=true" 
        item.update({"q": q})
    if not short:
        # Example URL query: "http://127.0.0.1:8000/users/24/items/sugar?q=I+am+king&short=false"
        item.update({"description": "This item has too long of a description"})
    return item