class GameState:

    def __init__(self):

        self.day = 1

        self.stress = 20
        self.information = 50

        self.water = 10
        self.food = 10

        self.inventory = [
            "radio",
            "flashlight",
            "book"
        ]

        self.running = True

    def clamp_values(self):

        self.stress = max(0, min(100, self.stress))
        self.information = max(0, min(100, self.information))

        self.water = max(0, self.water)
        self.food = max(0, self.food)

    def to_dict(self):

        return {
            "stress": self.stress,
            "information": self.information,
            "water": self.water,
            "food": self.food
        }