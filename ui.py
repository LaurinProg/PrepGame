from rich.console import Console
from rich.panel import Panel

console = Console()


def show_day_header(day):
    console.print(Panel(f"TAG {day}", style="bold white"))


def show_status(state):
    console.print(
        f"[bold]Stress:[/bold] {state['stress']} | "
        f"[bold]Info:[/bold] {state['information']} | "
        f"[bold]Wasser:[/bold] {state['water']} | "
        f"[bold]Nahrung:[/bold] {state['food']}"
    )


def show_event(text):
    console.print(f"\n[yellow]{text}[/yellow]\n")


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
