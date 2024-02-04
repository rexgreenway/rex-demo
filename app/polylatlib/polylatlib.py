# import polylatlib as pl
from fastapi import APIRouter

# Establish Router for PolyLatLib
pl_router = APIRouter()


@pl_router.get("/polylatlib")
async def polylatlib():
    return {"message": "PolyLatLib..."}
