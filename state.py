class GameState:

    def __init__(self):

        self.day = 1
        self.scenario = None

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
