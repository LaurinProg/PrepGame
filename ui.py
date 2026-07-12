from rich.console import Console
from rich.panel import Panel

console = Console()


def clear_screen():
    console.clear()


def render_game(state, items):
    clear_screen()
    show_day_header(state.day)
    show_status(state, items)
    show_inventory(state.inventory, items)


def show_day_header(day):
    console.print(
        Panel(
            f"TAG {day}",
            title="KRISENVERLAUF",
            style="bold white"
        )
    )


def create_bar(value, maximum=100, length=10):
    filled = int((value / maximum) * length)
    return "█" * filled + "░" * (length - filled)


def show_status(state, items):
    stress_bar = create_bar(state.stress)
    info_bar = create_bar(state.information)

    weight = calculate_weight(state.inventory, items)

    if state.stress >= 75:
        condition = "Kritische psychische Belastung"
    elif state.stress >= 50:
        condition = "Erhöhte Belastung"
    elif state.stress >= 25:
        condition = "Angespannte Lage"
    else:
        condition = "Stabile Situation"

    content = (
        f"Psychische Belastung:\n"
        f"{stress_bar} {state.stress}/100\n\n"
        f"Informationslage:\n"
        f"{info_bar} {state.information}/100\n\n"
        f"Gewicht:\n"
        f"{weight}/10\n\n"
        f"Lageeinschätzung:\n"
        f"{condition}"
    )

    console.print(
        Panel(
            content,
            title="STATUS",
            style="bold"
        )
    )


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


def show_event(text):
    console.print(
        f"\n[yellow]{text}[/yellow]\n"
    )


def show_atmosphere(text):
    console.print(
        f"\n[italic]{text}[/italic]"
    )


def choose_option(choices):
    console.print()

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