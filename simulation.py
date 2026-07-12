from ui import render_game, show_atmosphere, choose_option, clear_screen, show_phase, show_day_end
from state import GameState
from systems.resource_system import consume_resources
from systems.event_system import load_events, get_valid_events, get_random_event, apply_effects
from systems.stress_system import apply_stress_effects, apply_passive_stress
from systems.atmosphere_system import get_atmosphere_text
from systems.preparation_system import run_preparation_phase
from systems.inventory_system import has_item, get_quantity, load_items
from systems.item_effect_system import apply_passive_item_effects
from systems.action_system import run_actions
from systems.scenario_system import load_scenarios, choose_scenario, apply_scenario_effects
from systems.information_system import run_information_phase
from systems.analysis_system import show_analysis
from systems.crisis_system import update_crisis_phase
from systems.log_system import clear_log


def apply_event(state, event):
    effects = event["effects"]

    state.stress += effects.get("stress", 0)


def check_game_over(state):
    if get_quantity(state.inventory, "water") <= 0:
        print("\nIhr habt kein Wasser mehr.")
        state.running = False

    if get_quantity(state.inventory, "food") <= 0:
        print("\nIhr habt keine Nahrung mehr.")
        state.running = False

    if state.stress >= 100:
        print("\nDie Situation eskaliert völlig.")
        state.running = False


def run_simulation():
    state = GameState()

    clear_screen()
    scenarios = load_scenarios()
    scenario = choose_scenario(scenarios)
    state.scenario = scenario
    run_information_phase(scenario)
    apply_scenario_effects(state, scenario)

    run_preparation_phase(state)
    events = load_events()
    items = load_items()

    while state.running:
        update_crisis_phase(state)
        clear_log(state)

        render_game(state, items)

        consumed = consume_resources(state)

        show_phase(
            "VERSORGUNG",
            f"Wasser -{consumed['water']}\nNahrung -{consumed['food']}"
        )

        action_result = run_actions(state)
        show_phase(
            "AKTION",
            f"{action_result['name']}\n\n{action_result['text']}"
        )

        apply_passive_item_effects(state)
        apply_passive_stress(state)
        apply_stress_effects(state)

        valid_events = get_valid_events(state, events)
        event = get_random_event(valid_events)
        state.statistics["events_seen"] += 1
        show_phase("KRISENEREIGNIS", event["text"])

        choices = event["choices"]
        available_choices = []

        for choice in choices:
            requirements = choice.get("requires", [])
            allowed = True

            for req in requirements:
                if not has_item(state.inventory, req):
                    allowed = False

            if allowed:
                available_choices.append(choice)

        selected_choice = choose_option(available_choices)

        apply_effects(state, selected_choice["effects"], selected_choice.get("consume"))

        show_day_end(state)

        atmosphere_text = get_atmosphere_text(state)
        show_atmosphere(atmosphere_text)

        check_game_over(state)

        state.day += 1

        input("\nENTER für nächsten Tag...")

    show_analysis(state)