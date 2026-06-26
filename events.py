import json
import random
from pathlib import Path


def load_events():
    path = Path("data/events.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_random_event(events):
    return random.choice(events)