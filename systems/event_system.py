import json
import random
from pathlib import Path


def load_events():
    path = Path("data/events.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_valid_events(state, events):
    valid = []

    for event in events:
        conditions = event.get("conditions", {})
        required_items = conditions.get("requires", [])

        allowed = True

        for item in required_items:
            if item not in state.inventory:
                allowed = False

        if allowed:
            valid.append(event)

    return valid


def get_random_event(events):
    return random.choice(events)


def apply_effects(state, effects):
    state.stress += effects.get("stress", 0)
    state.information += effects.get("information", 0)
    state.clamp_values()