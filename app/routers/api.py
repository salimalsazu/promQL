from fastapi import APIRouter, HTTPException
import uuid

router = APIRouter()

data_store = []

# data post

@router.post("/data")
async def post_data(payload: dict):
    payload["id"] = str(uuid.uuid4())
    data_store.append(payload)
    return {
        "message": "Data stored",
        "item": payload,
        "current_count": len(data_store)
    }

# data get
@router.get("/data")
async def get_data():
    return {"data": data_store}


# data edit
@router.patch("/data/{item_id}")
async def patch_data(item_id: str, update: dict):
    for item in data_store:
        if item.get("id") == item_id:
            item.update(update)
            return {"message": "Item updated", "item": item}
    raise HTTPException(status_code=404, detail="Item not found")

# data delete
@router.delete("/data/{item_id}")
async def delete_data(item_id: str):
    for index, item in enumerate(data_store):
        if item.get("id") == item_id:
            deleted_item = data_store.pop(index)
            return {"message": "Item deleted", "item": deleted_item}
    raise HTTPException(status_code=404, detail="Item not found")
