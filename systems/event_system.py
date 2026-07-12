import json
import random
from pathlib import Path

from systems.inventory_system import has_item
from systems.effect_system import apply_effects


def load_events():
    path = Path("data/events.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_valid_events(state, events):
    valid = []

    for event in events:
        conditions = event.get("conditions", {})
        allowed = True

        required_items = conditions.get("requires", [])

        for item in required_items:
            if not has_item(state.inventory, item):
                allowed = False

        min_day = conditions.get("min_day")

        if min_day and state.day < min_day:
            allowed = False

        max_stress = conditions.get("max_stress")

        if max_stress and state.stress > max_stress:
            allowed = False

        required_modifiers = conditions.get("modifiers", [])

        for modifier in required_modifiers:
            if not state.modifiers.get(modifier, False):
                allowed = False

        if allowed:
            valid.append(event)

    return valid


def get_random_event(events):
    if not events:
        return {
            "text": "Ein ruhiger Tag vergeht.",
            "choices": [
                {
                    "text": "Weiter machen",
                    "effects": {}
                }
            ]
        }

    return random.choice(events)
