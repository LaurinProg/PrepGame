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


# ---------- Inventar ----------

def has_item(inventory, item_id):
    return inventory.get(item_id, 0) > 0


def get_quantity(inventory, item_id):
    return inventory.get(item_id, 0)


def add_item(inventory, item_id, amount=1):
    inventory[item_id] = get_quantity(inventory, item_id) + amount


def remove_item(inventory, item_id, amount=1):
    current = get_quantity(inventory, item_id)

    if current < amount:
        return False

    current -= amount

    if current == 0:
        del inventory[item_id]
    else:
        inventory[item_id] = current

    return True


# ---------- Auswertungen ----------

def calculate_inventory_weight(inventory, items):
    total_weight = 0

    for item_id, quantity in inventory.items():

        item = get_item_by_id(items, item_id)

        if item:
            total_weight += item.get("weight", 0) * quantity

    return total_weight


def get_items_by_tag(inventory, items, tag):
    matching_items = []

    for item_id in inventory.keys():

        item = get_item_by_id(items, item_id)

        if not item:
            continue

        if tag in item.get("tags", []):
            matching_items.append(item)

    return matching_items