from typing import List


class TeachingAssistant:
    name: str
    classes: List[str]
    infectivity: float
    chanceInfected: float

    def __init__(self, name, classes, infectivity):
        self.name = name
        self.classes = classes
        self.infectivity = infectivity
        chanceInfected = 0
