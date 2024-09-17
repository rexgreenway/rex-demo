# import polylatlib as pl
from fastapi import APIRouter

# Establish Router for PolyLatLib
bv_router = APIRouter()


@bv_router.get("/polylatlib")
async def braidvisualiser():
    return {"message": "BraidVisualiser..."}
