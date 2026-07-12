from systems.inventory_system import get_quantity, remove_item


def apply_passive_stress(state):
    water = get_quantity(state.inventory, "water")
    food = get_quantity(state.inventory, "food")

    if state.modifiers.get("isolation", False):
        state.stress += 3

    if water <= 3:
        state.stress += 6

    if food <= 3:
        state.stress += 4

    if state.information <= 30:
        state.stress += 5

    if state.information >= 70:
        state.stress -= 2

    state.clamp_values()


def apply_stress_effects(state):
    if state.stress >= 70:
        state.information -= 3

    if state.stress >= 85:
        remove_item(state.inventory, "food")

    state.clamp_values()