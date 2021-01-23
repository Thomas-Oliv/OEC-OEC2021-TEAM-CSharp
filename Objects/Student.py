from typing import List

import constants

class Student:
    id: int
    first: str
    last: str
    grade: int
    infectivity: float
    classes: List[str]
    extracurriculars: str
    chanceOfDisease: float  # from 0 to 1

    def __init__(self, id, firstname, lastname, grade, healthProblems, classes, extracurriculars):
        self.id = id
        self.grade = grade
        self.first = firstname
        self.last = lastname
        self.infectivity = 1.5**((grade + 5 - 14) / 2)
        if healthProblems:
            self.infectivity *= constants.HEALTH_CONDITION_MULTIPLIER
        self.classes = classes
        self.extracurriculars = extracurriculars
        self.chanceOfDisease = 0
