from typing import List


class TeachingAssistant:
    name: str
    classes: List[str]
    chanceInfected: float

    def __init__(self, name, classes, infectivity):
        self.name = name
        self.classes = classes
        chanceInfected = 0
