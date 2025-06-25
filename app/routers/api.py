from fastapi import APIRouter, Request

router = APIRouter()

data_store = []

@router.post("/data")
async def post_data(payload: dict):
    data_store.append(payload)
    return {"message": "Data stored", "current_count": len(data_store)}

@router.get("/data")
async def get_data():
    return {"data": data_store}
