import random


CALM_TEXTS = [
    "Die Situation wirkt momentan stabil.",
    "Noch scheint die Lage unter Kontrolle.",
    "Der Tag verläuft vergleichsweise ruhig."
]

TENSION_TEXTS = [
    "Die Anspannung wird zunehmend spürbar.",
    "Die Unsicherheit belastet alle merklich.",
    "Niemand spricht mehr besonders viel."
]

HIGH_STRESS_TEXTS = [
    "Die Stimmung kippt zunehmend.",
    "Kleine Probleme führen schnell zu Streit.",
    "Die Erschöpfung wird immer sichtbarer."
]

CRITICAL_TEXTS = [
    "Die Situation droht zu eskalieren.",
    "Panik breitet sich langsam aus.",
    "Kaum noch jemand kann ruhig schlafen."
]


def get_atmosphere_text(state):
    stress = state.stress

    if stress < 30:
        return random.choice(CALM_TEXTS)

    elif stress < 60:
        return random.choice(TENSION_TEXTS)

    elif stress < 85:
        return random.choice(HIGH_STRESS_TEXTS)

    return random.choice(CRITICAL_TEXTS)