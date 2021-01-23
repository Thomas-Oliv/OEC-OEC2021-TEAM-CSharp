from typing import List
import constants
from Objects.Student import Student
from Functions import computeNewChance


class ExtraCurricular:
    students: List[Student]

    def __init__(self, students):
        self.students = students

    def reduce(self):
        # dictionary containing all extracurriculars
        # add all students in extracurriculars to extracurricular dictionary
        for student in self.students:
            print(student.first)
            if student.extracurriculars is not None:
                constants.EXTRACURRICULARS[student.extracurriculars].append(student)
        # calculate increase in chance of disease for each extracurricular
        for key in constants.EXTRACURRICULARS:
            studentsExpectedToInfect = 0
            curricularSize = len(constants.EXTRACURRICULARS[key])
            for student in constants.EXTRACURRICULARS[key]:
                studentsExpectedToInfect += student.chanceOfDisease * constants.R_NAUGHT \
                                            / constants.EXTRACURRICULAR_SPACING_FACTOR
            for student in constants.EXTRACURRICULARS[key]:
                chanceInfected = (
                                             studentsExpectedToInfect - student.chanceOfDisease) / curricularSize * student.infectivity
                student.chanceOfDisease = computeNewChance(student.chanceOfDisease, chanceInfected)
