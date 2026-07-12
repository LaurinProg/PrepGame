def log(state, category, text):
    state.daily_log.append({
        "category": category,
        "text": text
    })


def clear_log(state):
    state.daily_log.clear()