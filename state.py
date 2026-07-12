class GameState:

    def __init__(self):

        self.day = 1

        self.stress = 20
        self.information = 50

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

    def to_dict(self):
        return {
            "stress": self.stress,
            "information": self.information,
            "water": self.inventory.get("water", 0),
            "food": self.inventory.get("food", 0)
        }