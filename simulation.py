from events import load_events, get_random_event
from ui import show_day_header, show_status, show_event


class GameState:
    def __init__(self):
        self.day = 1
        self.stress = 20
        self.water = 10
        self.food = 10

        self.information = 50

        self.inventory = [
            "radio",
            "flashlight",
            "book"
        ]

        self.running = True


def consume_resources(state):
    state.water -= 1
    state.food -= 1

    if state.water <= 3:
        state.stress += 10

    if state.food <= 3:
        state.stress += 5


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

    events = load_events()

    while state.running:

        show_day_header(state.day)

        consume_resources(state)

        event = get_random_event(events)

        show_event(event["text"])

        apply_event(state, event)

        show_status(state.to_dict())

        check_game_over(state)

        state.day += 1

        input("\nENTER für nächsten Tag...")