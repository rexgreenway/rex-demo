from pydantic import BaseModel


class RegularPolygon(BaseModel):
    """
    Regular Polygon ...
    """

    name: str
    description: str | None = None
    no_of_sides: int
    edges: list[tuple]
    vertices: list
