def consume_resources(state):
    state.water -= 1
    state.food -= 1

    state.clamp_values()
