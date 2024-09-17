from fastapi import APIRouter

photography_router = APIRouter()


@photography_router.get("/photography")
async def photography():
    return {"message": "Photography..."}
