from systems.inventory_system import remove_item, get_item_name
from systems.log_system import log


def apply_effects(state, effects, consume=None):
    stress = effects.get("stress", 0)
    information = effects.get("information", 0)

    if stress:
        state.stress += stress
        sign = "+" if stress > 0 else ""
        log(state, "stress", f"Stress {sign}{stress}")

    if information:
        state.information += information
        sign = "+" if information > 0 else ""
        log(state, "information", f"Information {sign}{information}")

    if consume:
        for item_id, amount in consume.items():
            remove_item(state.inventory, item_id, amount)
            log(state, "resource", f"{get_item_name(item_id)} verbraucht (-{amount})")

    state.clamp_values()