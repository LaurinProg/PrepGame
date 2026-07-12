from rich.console import Console
from rich.panel import Panel

console = Console()

def clear_screen():
    console.clear()


def show_day_header(day):
    console.print(Panel(f"TAG {day}", style="bold white"))


def show_status(state):
    console.print(
        f"[bold]Stress:[/bold] {state['stress']} | "
        f"[bold]Info:[/bold] {state['information']} | "
        f"[bold]Wasser:[/bold] {state['water']} | "
        f"[bold]Nahrung:[/bold] {state['food']}"
    )


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
    console.print(f"\n[yellow]{text}[/yellow]\n")


def show_atmosphere(text):
    console.print(f"\n[italic]{text}[/italic]")


def choose_option(choices):

    console.print()

    for index, choice in enumerate(choices, start=1):
        console.print(f"{index}. {choice['text']}")

    while True:

        user_input = input("\nEntscheidung: ")

        if user_input.isdigit():

            number = int(user_input)

            if 1 <= number <= len(choices):
                return choices[number - 1]
