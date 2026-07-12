class GameState:

    def __init__(self):

        self.day = 1
        self.scenario = None
        self.modifiers = {}

        self.stress = 20
        self.information = 50

        self.crisis_phase = "Schockphase"

        self.statistics = {
            "starting_stress": self.stress,
            "highest_stress": self.stress,
            "water_consumed": 0,
            "food_consumed": 0,
            "battery_used": 0,
            "items_used": 0,
            "events_seen": 0,
            "actions_taken": 0,
            "stress_sources": {}
        }

        self.inventory = {
            "water": 10,
            "food": 10,
            "radio": 1,
            "flashlight": 1,
            "book": 1
        }

        self.running = True

    def clamp_values(self):
        self.stress = max(0, min(100, self.stress))
        self.information = max(0, min(100, self.information))

        if self.stress > self.statistics["highest_stress"]:
            self.statistics["highest_stress"] = self.stress
