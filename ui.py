from rich.console import Console
from rich.panel import Panel

console = Console()


def clear_screen():
    console.clear()


def render_game(state, items):
    clear_screen()
    show_day_header(state.day)
    show_status(state)
    show_inventory(state.inventory, items)


def show_day_header(day):
    console.print(Panel(f"TAG {day}", style="bold white"))


def show_status(state):
    stress_text = f"[bold]Stress:[/bold] {state.stress}/100"
    info_text = f"[bold]Information:[/bold] {state.information}/100"

    console.print(
        f"{stress_text} | {info_text}"
    )

    if state.stress >= 75:
        console.print("[red]Die Belastung ist sehr hoch.[/red]")

    elif state.stress >= 50:
        console.print("[yellow]Die Situation wird zunehmend belastend.[/yellow]")


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