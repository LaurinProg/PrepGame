from systems.inventory_system import remove_item


def apply_effects(state, effects, consume=None):
    state.stress += effects.get("stress", 0)
    state.information += effects.get("information", 0)

    if consume:
        for item_id, amount in consume.items():
            remove_item(
                state.inventory,
                item_id,
                amount
            )

    state.clamp_values()