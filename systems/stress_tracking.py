def add_stress(state, amount, reason):
    state.stress += amount

    sources = state.statistics["stress_sources"]

    if reason not in sources:
        sources[reason] = 0

    sources[reason] += amount

    state.clamp_values()