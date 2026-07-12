import json
import random
from pathlib import Path

from systems.inventory_system import has_item, remove_item


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
            if not has_item(state.inventory, item):
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


def apply_effects(state, effects, consume=None):
    state.stress += effects.get("stress", 0)
    state.information += effects.get("information", 0)

    if consume:
        for item_id, amount in consume.items():
            remove_item(
                state.inventory,
                item_id,
                amount
            )

    state.clamp_values()