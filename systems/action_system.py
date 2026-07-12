from systems.inventory_system import has_item, remove_item
from systems.effect_system import apply_effects

ACTIONS = {
    "radio": {
        "name": "Radio hören",
        "description": "Kann neue Informationen liefern und beruhigen.",
        "requirements": ["radio", "battery"]
    },
    "book": {
        "name": "Buch lesen",
        "description": "Eine ruhige Beschäftigung kann helfen, Stress abzubauen.",
        "requirements": ["book"]
    },
    "nothing": {
        "name": "Nichts tun",
        "description": "Keine Ressourcen verbraucht, aber die Belastung bleibt bestehen.",
        "requirements": []
    }
}

def get_available_actions(state):
    actions = []

    if has_item(state.inventory, "radio") and has_item(state.inventory, "battery"):
        actions.append("radio")

    if has_item(state.inventory, "book"):
        actions.append("book")

    actions.append("nothing")

    return actions


def show_actions(actions):
    print("\nWas möchtest du tun?\n")

    for index, action_id in enumerate(actions, start=1):
        action = ACTIONS[action_id]

        print(f"{index}. {action['name']}")
        print(f"   {action['description']}")


def execute_action(state, action):
    state.statistics["actions_taken"] += 1

    result = {
        "name": ACTIONS[action]["name"],
        "text": ""
    }

    if action == "radio":
        apply_effects(state, {"information": 8, "stress": -3}, {"battery": 1})
        result["text"] = "Neue Informationen wurden empfangen."

    elif action == "book":
        apply_effects(state, {"stress": -5})
        result["text"] = "Die Ruhephase hilft, Stress abzubauen."

    elif action == "nothing":
        apply_effects(state, {"stress": -1})
        result["text"] = "Die Zeit vergeht ohne besondere Ereignisse."

    return result


def run_actions(state):
    actions = get_available_actions(state)

    show_actions(actions)

    while True:
        choice = input("\nAuswahl: ")

        if choice.isdigit():
            index = int(choice) - 1

            if 0 <= index < len(actions):
                result = execute_action(state, actions[index])
                break

    state.clamp_values()
    return result