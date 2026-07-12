from systems.inventory_system import remove_item


def consume_resources(state):
    water_usage = 1

    if state.modifiers.get("water_pressure", False):
        water_usage = 2

    remove_item(
        state.inventory,
        "water",
        water_usage
    )

    remove_item(
        state.inventory,
        "food"
    )