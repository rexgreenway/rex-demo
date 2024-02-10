import polylatlib as pl


def build_regular_polygon(sides: int) -> tuple[str, pl.RegularPolygon]:
    match sides:
        case 3:
            polygon = pl.EquilateralTriangle()
            name = "EquilateralTriangle"

        case 4:
            polygon = pl.Square()
            name = "Square"

        case 5:
            polygon = pl.Pentagon()
            name = "Pentagon"

        case 6:
            polygon = pl.Hexagon()
            name = "Hexagon"

        case 7:
            polygon = pl.Septagon()
            name = "Septagon"

        case 8:
            polygon = pl.Octagon()
            name = "Octagon"

        case _:
            polygon = pl.RegularPolygon(sides)
            name = f"RegularPolygon_{sides}"

    return (
        name,
        polygon,
    )
