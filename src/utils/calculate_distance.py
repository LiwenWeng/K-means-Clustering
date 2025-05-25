import math
from src.geometry_types import Point


def calculate_distance(point_a: Point, point_b: Point) -> float:
    x_a, y_a = point_a
    x_b, y_b = point_b

    return math.sqrt((x_b - x_a)**2 + (y_b - y_a)**2)