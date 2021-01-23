from typing import List


class TeachingAssistant:
    first: str
    last: str
    classes: List[str]
    chanceInfected: float

    def __init__(self, first,last, classes):
        self.first = first
        self.last = last
        self.classes = classes
        chanceInfected = 0
