from systems.inventory_system import remove_item, get_quantity
from systems.log_system import log


def consume_resources(state):
    consumed = {
        "water": 0,
        "food": 0
    }

    water_usage = 1

    if state.modifiers.get("water_pressure", False):
        water_usage = 2
        log(state, "resource", "Erhöhter Wasserverbrauch")

    if get_quantity(state.inventory, "water") >= water_usage:
        remove_item(state.inventory, "water", water_usage)
        state.statistics["water_consumed"] += water_usage
        consumed["water"] = water_usage
        log(state, "resource", f"Wasser verbraucht (-{water_usage})")

    if get_quantity(state.inventory, "food") >= 1:
        remove_item(state.inventory, "food")
        state.statistics["food_consumed"] += 1
        consumed["food"] = 1
        log(state, "resource", "Nahrung verbraucht (-1)")

    return consumed