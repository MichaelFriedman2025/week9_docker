from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import json
import uvicorn

app = FastAPI(title="server2")

DB_PATH = Path("db/shopping_list.json")

DATA_PATH = Path("data/backup_shopping_list.json")

class Item(BaseModel):
    name:str
    quantity: int


@app.get("/items")
def return_all_items() -> list:
    with open(DB_PATH, "r") as f:
        return json.load(f)

@app.post("/items")
def add_item(item:Item):
    if not DB_PATH.exists():
        data = []
    else:
        with open(DB_PATH, "r") as f:
            data = json.load(f)
    len_data = len(data)
    data.append({"id":len_data + 1,"name":item.name,"quantity":item.quantity})
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)
    return {"all items":data}

@app.get("/backup")
def reads_items():
    with open(DATA_PATH, "r") as f:
        return json.load(f)
    
@app.get("/backup/save")
def reads_items():
    try:
        with open(DB_PATH, "r") as f:
            data = json.load(f)
        with open(DATA_PATH, "w") as f:
            json.dump(data, f, indent=4)
        return {"massage":"Copy completed successfully."}
    except Exception as e:
        return {"massage":f"{e}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)