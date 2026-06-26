from ui import show_day_header, show_status, show_event, show_atmosphere, choose_option

from state import GameState
from systems.resource_system import consume_resources
from systems.event_system import load_events, get_valid_events, get_random_event, apply_effects
from systems.stress_system import apply_stress_effects, apply_passive_stress
from systems.atmosphere_system import get_atmosphere_text
from systems.preparation_system import run_preparation_phase
from systems.inventory_system import has_item
from systems.item_effect_system import apply_passive_item_effects


def apply_event(state, event):
    effects = event["effects"]

    state.stress += effects.get("stress", 0)


def check_game_over(state):
    if state.water <= 0:
        print("\nIhr habt kein Wasser mehr.")
        state.running = False

    if state.stress >= 100:
        print("\nDie Situation eskaliert völlig.")
        state.running = False


def run_simulation():
    state = GameState()
    run_preparation_phase(state)
    events = load_events()

    while state.running:

        show_day_header(state.day)

        consume_resources(state)
        apply_passive_item_effects(state)
        apply_passive_stress(state)
        apply_stress_effects(state)

        valid_events = get_valid_events(state, events)
        event = get_random_event(valid_events)
        show_event(event["text"])

        choices = event["choices"]
        available_choices = []

        for choice in choices:
            requirements = choice.get("requires", [])
            allowed = True

            for req in requirements:
                if not has_item(state, req):
                    allowed = False

            if allowed:
                available_choices.append(choice)

        selected_choice = choose_option(available_choices)

        apply_effects(state, selected_choice["effects"])

        show_status(state.to_dict())
        atmosphere_text = get_atmosphere_text(state)
        show_atmosphere(atmosphere_text)

        check_game_over(state)

        state.day += 1

        input("\nENTER für nächsten Tag...")