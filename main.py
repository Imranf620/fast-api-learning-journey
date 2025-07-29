from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the Pydantic model for request body
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True  # default value

# GET Endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# POST Endpoint using Pydantic
@app.post("/submit")
def submit_item(item: Item):
    return {
        "received": {
            "name": item.name,
            "price": item.price,
            "in_stock": item.in_stock
        }
    }
