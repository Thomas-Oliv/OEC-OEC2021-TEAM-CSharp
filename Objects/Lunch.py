from typing import List

from constants import R_NAUGHT
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
            studentsExpectedToInfect += student.chanceOfDisease * R_NAUGHT

        studentInfectionProbability = studentsExpectedToInfect / lunchSize
        for student in self.students:
            chanceInfected = studentInfectionProbability * student.infectivity
            student.chanceOfDisease = computeNewChance(chanceInfected, student.chanceOfDisease)
