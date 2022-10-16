# Author: Husain Al Zerjawi
# Purpose: Query Parameters and String Validations
# Date: 16/10/2022

from pydantic import Required
from fastapi import FastAPI, Query

app = FastAPI()

# @app.get("/items/")
# async def read_items(q: str | None = Query(default=None, max_length=50, min_length=3, regex="^fixedquery$")):
#     results = {"items": [{"item_id": "Cheese"}, {"item_id": "Bread"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: str = Query(max_length=50, min_length=3)):
#     results = {"items": [{"item_id": "Cheese"}, {"item_id": "Bread"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: str = Query(default=..., max_length=50, min_length=3)):
#     results = {"items": [{"item_id": "Cheese"}, {"item_id": "Bread"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: str = Query(default=Required, max_length=50, min_length=3)):
#     results = {"items": [{"item_id": "Cheese"}, {"item_id": "Bread"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: list[str] | None = Query(default=["king", "queen"])):
#     query_items = {"q": q}
#     return query_items

@app.get("/items/")
async def read_items(
    q: str | None = Query(
        default=None, 
        title="Query string", 
        min_length=3,
        description="Query string for the items to search in the database that have a good match",
        alias="item-query",
        deprecated=True)

):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results