from fastapi import APIRouter

bv_router = APIRouter()


@bv_router.get("/braidvisualiser")
async def braidvisualiser():
    return {"message": "BraidVisualiser..."}
