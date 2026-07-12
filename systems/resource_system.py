from systems.inventory_system import remove_item, get_quantity


def consume_resources(state):
    water_usage = 1

    if state.modifiers.get("water_pressure", False):
        water_usage = 2

    if get_quantity(state.inventory, "water") >= water_usage:
        remove_item(
            state.inventory,
            "water",
            water_usage
        )

        state.statistics["water_consumed"] += water_usage

    if get_quantity(state.inventory, "food") >= 1:
        remove_item(
            state.inventory,
            "food"
        )

        state.statistics["food_consumed"] += 1