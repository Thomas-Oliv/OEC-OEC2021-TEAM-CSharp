from typing import List

import constants

class Student:
    id: int
    grade: int
    infectivity: float
    classes: List[str]
    extracurriculars: List[str]
    chanceOfDisease: float  # from 0 to 1

    def __init__(self, id, grade, healthProblems, classes, extracurriculars):
        self.id = id
        self.grade = grade
        self.infectivity = (healthProblems * constants.HEALTH_CONDITION_MULTIPLIER * 1.5**(grade + 5 - 14))
        self.classes = classes
        self.extracurriculars = extracurriculars
        self.chanceOfDisease = 0
