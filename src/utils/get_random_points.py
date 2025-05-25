import random
from src.geometry_types import Coordinates, Point


def get_random_points(coordinates: Coordinates, amount: int) -> list[Point]:
    return random.sample(list(coordinates), amount)