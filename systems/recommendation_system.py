import json
from pathlib import Path


def load_recommendations():
    path = Path("data/recommendations.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def evaluate_recommendations(state, recommendations):
    results = []

    for recommendation in recommendations:

        result = {
            "title": recommendation["title"],
            "recommendation": recommendation["recommendation"],
            "status": "neutral"
        }

        if recommendation["evaluate"] == "quantity":

            amount = 0

            for item in recommendation["related_items"]:
                amount += state.inventory.get(item, 0)

            target = recommendation.get("target", 1)

            if amount >= target:
                result["status"] = "gut vorbereitet"

            elif amount >= target / 2:
                result["status"] = "teilweise vorbereitet"

            else:
                result["status"] = "kritische Reserve"

        elif recommendation["evaluate"] == "presence":

            found = False

            for item in recommendation["related_items"]:
                if state.inventory.get(item, 0) > 0:
                    found = True

            if found:
                result["status"] = "vorbereitet"
            else:
                result["status"] = "fehlend"

        elif recommendation["evaluate"] == "stress":

            if state.statistics["highest_stress"] < 60:
                result["status"] = "stabil"
            else:
                result["status"] = "belastet"

        results.append(result)

    return results