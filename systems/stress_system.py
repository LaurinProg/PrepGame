def apply_passive_stress(state):
    if state.water <= 3:
        state.stress += 6

    if state.food <= 3:
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
        state.food -= 1

    state.clamp_values()
