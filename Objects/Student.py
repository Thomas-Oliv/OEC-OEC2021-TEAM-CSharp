from typing import List

import constants

class Student:
    id: int
    grade: int
    infectivity: float
    classes: List[str]
    extracurriculars: List[str]
    chanceOfDisease: float  # from 0 to 1

    def __init__(self, id, grade, infectivity, classes, extracurriculars):
        self.id = id
        self.grade = grade
        self.infectivity = infectivity
        self.classes = classes
        self.extracurriculars = extracurriculars
        self.chanceOfDisease = 0

    def calcInfectivity(healthProblems): 
        # healthProblems is a boolean (0 or 1) -> Apply factor if healthProblems == true
        # Multiply by age factor which is grade + 5 (grade 9 = 14 years old) - 14 (to normalize value)
        return (healthProblems * constants.HEALTH_CONDITION_MULTIPLIER * (1.5 ** (self.grade + 5 - 14)))