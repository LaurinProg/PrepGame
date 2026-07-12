from systems.inventory_system import get_quantity, remove_item
from systems.stress_tracking import add_stress


def apply_passive_stress(state):
    water = get_quantity(state.inventory, "water")
    food = get_quantity(state.inventory, "food")

    if state.modifiers.get("isolation", False):
        state.stress += 3

    if water <= 3:
        add_stress(state, 4, "Wassermangel")

    if food <= 3:
        add_stress(state, 3, "Nahrungsmangel")

    if state.information <= 30:
        add_stress(state, 3, "Informationsmangel")

    if state.information >= 70:
        state.stress -= 2

    state.clamp_values()


def apply_stress_effects(state):
    if state.stress >= 70:
        state.information -= 2

    if state.stress >= 85:
        state.information -= 5

    state.clamp_values()