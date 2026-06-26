import json
from pathlib import Path


def load_items():
    path = Path("data/items.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)