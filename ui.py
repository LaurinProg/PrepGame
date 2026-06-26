from rich.console import Console
from rich.panel import Panel

console = Console()


def show_day_header(day):
    console.print(Panel(f"TAG {day}", style="bold white"))


def show_status(state):
    console.print(
        f"[bold]Stress:[/bold] {state['stress']} | "
        f"[bold]Wasser:[/bold] {state['water']} | "
        f"[bold]Nahrung:[/bold] {state['food']}"
    )


def show_event(text):
    console.print(f"\n[yellow]{text}[/yellow]\n")