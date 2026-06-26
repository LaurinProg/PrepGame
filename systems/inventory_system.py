import json
from pathlib import Path


def load_items():
    path = Path("data/items.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_item_by_id(items, item_id):
    for item in items:

        if item["id"] == item_id:
            return item

    return None


def has_item(state, item_id):
    return item_id in state.inventory


def calculate_inventory_weight(state, items):
    total_weight = 0

    for item_id in state.inventory:

        item = get_item_by_id(items, item_id)

        if item:
            total_weight += item.get("weight", 0)

    return total_weight


def get_items_by_tag(state, items, tag):
    matching_items = []

    for item_id in state.inventory:

        item = get_item_by_id(items, item_id)

        if not item:
            continue

        tags = item.get("tags", [])

        if tag in tags:
            matching_items.append(item)

    return matching_items