from rich.console import Console
from rich.panel import Panel

console = Console()


def show_analysis(state):

    stats = state.statistics

    console.clear()

    console.print(
        Panel(
            "KRISENANALYSE",
            style="bold cyan"
        )
    )

    if state.scenario:
        console.print(
            f"\n[bold]Szenario:[/bold] {state.scenario['name']}"
        )

    console.print(
        f"\nÜberstandene Tage: {state.day - 1}"
    )

    console.print("\n[bold]Versorgung:[/bold]")
    console.print(
        f"- Wasser verbraucht: {stats['water_consumed']}"
    )
    console.print(
        f"- Nahrung verbraucht: {stats['food_consumed']}"
    )

    console.print("\n[bold]Psychische Belastung:[/bold]")
    console.print(
        f"- Startstress: {stats['starting_stress']}"
    )
    console.print(
        f"- Höchster Stress: {stats['highest_stress']}"
    )

    console.print("\n[bold]Entscheidungen:[/bold]")
    console.print(
        f"- Ereignisse erlebt: {stats['events_seen']}"
    )
    console.print(
        f"- Aktionen durchgeführt: {stats['actions_taken']}"
    )

    show_stress_sources(stats)


def show_stress_sources(stats):

    sources = stats["stress_sources"]

    if not sources:
        return

    console.print("\n[bold]Hauptbelastungen:[/bold]")

    sorted_sources = sorted(
        sources.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for name, value in sorted_sources:
        console.print(
            f"- {name}: +{value}"
        )