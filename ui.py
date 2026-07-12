from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.table import Table
from config import MAX_INVENTORY_WEIGHT

console = Console()


def clear_screen():
    console.clear()


def render_game(state, items):
    clear_screen()

    show_day_header(state.day)

    console.print(
        Columns(
            [
                create_status_panel(state, items),
                create_inventory_panel(state, items)
            ],
            equal=True
        )
    )


def show_day_header(day):
    console.print(
        Panel(
            f"TAG {day}",
            title="KRISENVERLAUF",
            style="bold white"
        )
    )


def create_status_panel(state, items):
    stress_bar = create_bar(state.stress)
    info_bar = create_bar(state.information)

    weight = calculate_weight(state.inventory, items)

    if state.stress >= 75:
        condition = "Kritisch"
    elif state.stress >= 50:
        condition = "Belastet"
    elif state.stress >= 25:
        condition = "Angespannt"
    else:
        condition = "Stabil"

    content = (
        f"Phase: {state.crisis_phase}\n\n"
        f"Stress: {stress_bar} {state.stress}\n"
        f"Info:   {info_bar} {state.information}\n\n"
        f"Gewicht: {weight}/{MAX_INVENTORY_WEIGHT}\n"
        f"Lage: {condition}"
    )

    return Panel(content, title="STATUS")


def create_inventory_panel(state, items):

    table = Table(
        show_header=False,
        box=None
    )

    table.add_column()

    for item in items:
        quantity = state.inventory.get(item["id"], 0)

        if quantity > 0:
            table.add_row(f"{item['name']}: x{quantity}")

    return Panel(table, title="INVENTAR")


def create_bar(value, maximum=100, length=10):
    filled = int((value / maximum) * length)
    return "█" * filled + "░" * (length - filled)


def show_phase(title, text):
    console.print(Panel(text, title=title))


def calculate_weight(inventory, items):
    total = 0

    for item in items:
        quantity = inventory.get(item["id"], 0)

        if quantity > 0:
            total += item["weight"] * quantity

    return total


def show_inventory(inventory, items):
    console.print("\n[bold]Inventar:[/bold]")

    if not inventory:
        console.print("Keine Gegenstände vorhanden.")
        return

    for item in items:
        quantity = inventory.get(item["id"], 0)

        if quantity > 0:
            console.print(
                f"- {item['name']} x{quantity}"
            )


def show_atmosphere(text):
    console.print(
        f"\n[italic]{text}[/italic]"
    )


def choose_option(choices):
    console.print(
        Panel(
            "Welche Entscheidung triffst du?",
            title="ENTSCHEIDUNG"
        )
    )

    for index, choice in enumerate(choices, start=1):
        console.print(
            f"{index}. {choice['text']}"
        )

    while True:
        user_input = input("\nEntscheidung: ")

        if user_input.isdigit():
            number = int(user_input)

            if 1 <= number <= len(choices):
                return choices[number - 1]


def show_day_end(state):
    if state.stress >= 75:
        condition = "Kritische Belastung"
    elif state.stress >= 50:
        condition = "Belastete Lage"
    elif state.stress >= 25:
        condition = "Angespannte Lage"
    else:
        condition = "Stabile Lage"

    content = (
        f"Stress: {state.stress}/100\n"
        f"Information: {state.information}/100\n"
        f"Lage: {condition}"
    )

    categories = {
        "resource": "Versorgung",
        "action": "Aktionen",
        "event": "Ereignisse",
        "stress": "Stress"
    }

    log_text = ""

    for category, title in categories.items():
        entries = [
            entry["text"]
            for entry in state.daily_log
            if entry["category"] == category
        ]

        if not entries:
            continue

        log_text += f"\n{title}\n"

        for entry in entries:
            log_text += f"• {entry}\n"

    content += log_text

    console.print(Panel(content, title="TAGESENDE"))
