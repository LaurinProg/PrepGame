import json
from pathlib import Path


def load_scenarios():
    path = Path("data/scenarios.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_scenario(scenarios, scenario_id):
    for scenario in scenarios:
        if scenario["id"] == scenario_id:
            return scenario

    return None


def apply_scenario_effects(state, scenario):
    effects = scenario.get("effects", {})

    state.stress += effects.get("stress", 0)
    state.information += effects.get("information", 0)

    state.clamp_values()


def choose_scenario(scenarios):
    print("\nWelche Krise erwartet euch?\n")

    for index, scenario in enumerate(scenarios, start=1):
        print(
            f"{index}. {scenario['name']}"
        )
        print(
            f"   {scenario['description']}"
        )

    while True:
        choice = input("\nAuswahl: ")

        if choice.isdigit():
            index = int(choice) - 1

            if 0 <= index < len(scenarios):
                return scenarios[index]