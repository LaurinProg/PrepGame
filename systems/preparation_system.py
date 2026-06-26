from rich.console import Console

from systems.inventory_system import load_items

console = Console()

MAX_WEIGHT = 10


def calculate_selected_weight(selected_items):
    total = 0

    for item in selected_items:
        total += item.get("weight", 0)

    return total


def show_selected_items(selected_items):
    console.print("\n[bold]Ausgewählte Gegenstände:[/bold]")

    if not selected_items:
        console.print("Noch keine Gegenstände ausgewählt.")
        return

    for item in selected_items:
        console.print(
            f"- {item['name']} "
            f"(Gewicht: {item['weight']})"
        )


def show_available_items(items):

    console.print("\n[bold]Verfügbare Gegenstände:[/bold]\n")

    for index, item in enumerate(items, start=1):

        console.print(
            f"{index}. "
            f"{item['name']} "
            f"(Gewicht: {item['weight']})"
        )

        console.print(
            f"   {item['description']}"
        )


def run_preparation_phase(state):
    items = load_items()
    selected_items = []

    while True:
        console.clear()
        current_weight = calculate_selected_weight(selected_items)

        console.print("\n[bold cyan]VORBEREITUNGSPHASE[/bold cyan]")
        console.print("\nDu kannst Vorräte für die Krise auswählen.")

        console.print(f"\nMaximales Gewicht: {MAX_WEIGHT}")
        console.print(f"Aktuelles Gewicht: {current_weight}")

        show_selected_items(selected_items)
        show_available_items(items)

        console.print("\n0. Vorbereitung abschließen")

        choice = input("\nAuswahl: ")

        if choice == "0":
            break

        if not choice.isdigit():
            continue

        index = int(choice) - 1

        if index < 0 or index >= len(items):
            continue

        item = items[index]

        new_weight = (current_weight + item["weight"])

        if new_weight > MAX_WEIGHT:
            console.print("\n[red]Dieses Gewicht kann nicht mehr getragen werden.[/red]")

            input("\nENTER drücken...")
            continue

        selected_items.append(item)

    state.inventory = [
        item["id"]
        for item in selected_items
    ]