from src.geometry_types import Coordinates
from typing import Callable
import csv

def extract_csv_file(file_path: str) -> Coordinates:
    try: 
        with open(file_path, 'r') as file:
            coordinates = list(csv.reader(file))
            return [tuple(map(float, p)) for p in coordinates]
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")

def process_csv_file(file_path: str, func: Callable[[Coordinates], None], *args) -> None:
    return func(extract_csv_file(file_path), *args)
