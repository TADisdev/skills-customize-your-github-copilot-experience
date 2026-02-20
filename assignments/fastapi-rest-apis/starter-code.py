from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI Assignment Starter")


class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=300)


items = []


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def create_item(payload: ItemCreate):
    item_id = len(items) + 1
    item = {
        "id": item_id,
        "name": payload.name,
        "description": payload.description,
    }
    items.append(item)
    return item


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
