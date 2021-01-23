from typing import List

from Objects.Student import Student
from Functions import computeNewChance


class Lunch:
    students: List[Student]

    def __init__(self, students):
        self.students = students

    def reduce(self):
        studentsExpectedToInfect = 0

        lunchSize = len(self.students)
        for student in self.students:
            # 3 is the r0 value
            studentsExpectedToInfect += student.chanceOfDisease * 3

        studentInfectionProbability = studentsExpectedToInfect / lunchSize
        for student in self.students:
            chanceInfected = studentInfectionProbability * student.infectivity
            student.chanceOfDisease = computeNewChance(chanceInfected, student.chanceOfDisease)
