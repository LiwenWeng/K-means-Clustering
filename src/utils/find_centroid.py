from functools import reduce
from src.geometry_types import Coordinates, Point


def find_centroid(coordinates: Coordinates) -> Point:
    total = reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), coordinates)
    return (total[0] / len(coordinates), total[1] / len(coordinates))