from systems.inventory_system import load_items, get_items_by_tag


def apply_passive_item_effects(state):
    items = load_items()

    information_items = get_items_by_tag(state.inventory, items, "information")

    if information_items:
        state.information += 3
    else:
        state.information -= 5

    entertainment_items = get_items_by_tag(state.inventory, items,"entertainment")

    if entertainment_items:
        state.stress -= 2

    light_items = get_items_by_tag(state.inventory, items,"light")

    if light_items:
        state.stress -= 1
    else:
        state.stress += 3

    medical_items = get_items_by_tag(state.inventory, items,"medical")

    if medical_items and state.stress >= 80:
        state.stress -= 2

    state.clamp_values()