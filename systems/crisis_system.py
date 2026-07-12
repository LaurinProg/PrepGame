def update_crisis_phase(state):
    day = state.day

    if day <= 2:
        state.crisis_phase = "Schockphase"
    elif day <= 5:
        state.crisis_phase = "Anpassungsphase"
    else:
        state.crisis_phase = "Erschöpfungsphase"