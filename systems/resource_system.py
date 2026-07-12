from systems.inventory_system import remove_item


def consume_resources(state):
    remove_item(state.inventory, "water")
    remove_item(state.inventory, "food")