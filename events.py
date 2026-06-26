import json
import random
from pathlib import Path


def load_events():
    path = Path("data/events.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_random_event(events):
    return random.choice(events)


def event_matches_conditions(state, event):

    conditions = event.get("conditions", {})

    required_items = conditions.get("requires", [])

    for item in required_items:
        if item not in state.inventory:
            return False

    return True