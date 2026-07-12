from rich.console import Console

console = Console()


def run_information_phase(scenario):
    console.clear()

    console.print("\n[bold cyan]INFORMATIONSPHASE[/bold cyan]\n")

    console.print(
        "Es gibt erste Hinweise auf eine kommende Krise.\n"
    )

    console.print(
        f"[yellow]{scenario['description']}[/yellow]\n"
    )

    console.print(
        "Die Informationen sind unvollständig. "
        "Bereite dich so gut wie möglich vor."
    )

    input("\nENTER drücken, um fortzufahren...")