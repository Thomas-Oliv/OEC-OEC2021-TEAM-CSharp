from typing import List


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
