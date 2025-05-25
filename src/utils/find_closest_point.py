from src.geometry_types import Point
from src.utils import calculate_distance


def find_closest_point(origin: Point, points: list[Point]) -> Point:
    return min(points, key=lambda p: calculate_distance(origin, p))