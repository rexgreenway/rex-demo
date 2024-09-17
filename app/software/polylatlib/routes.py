from fastapi import APIRouter

from .models import RegularPolygon
from .utils import build_regular_polygon

# Establish Router for PolyLatLib
pl_router = APIRouter()


@pl_router.get("/polylatlib")
async def polylatlib() -> dict[str, str]:
    return {"message": "PolyLatLib"}


@pl_router.get("/polylatlib/polygon")
async def polygon() -> dict[str, str]:
    return {"message": "PolyLatLib - Polygon"}


@pl_router.get("/polylatlib/polygon/{sides}")
async def get_regular_polygon(sides: int) -> RegularPolygon:
    name, polygon = build_regular_polygon(sides)
    return RegularPolygon(name=name, no_of_sides=sides, edges=polygon.edges, vertices=polygon.vertices)
