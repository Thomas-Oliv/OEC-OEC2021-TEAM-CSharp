from typing import List

import constants

from Objects.TeachingAssistant import TeachingAssistant
from Objects.Student import Student
from Objects.Teacher import Teacher


class ClassPeriod:
    name: str
    period: int
    students: List[Student]
    ta: TeachingAssistant
    teacher: Teacher
    contaminationMultiplier: float

    def __init__(self, name, period, students, ta, teacher):
        self.name = name
        self.period = period
        self.students = students
        self.ta = ta
        self.teacher = teacher
        self.infectedMultiplier = 0

    def reducePeriod(self):
        studentsExpectedToInfect = 0
        teacherExpectedToInfect = 0
        teacherAssistantExpectedToInfect = 0

        for student in self.students:
            # 3 is the r0 value
            studentsExpectedToInfect += student.chanceOfDisease * 3

        teacherExpectedToInfect += self.teacher.chanceInfected * 3
        teacherAssistantExpectedToInfect += self.ta.chanceInfected * 3

        numStudents = len(self.students)
        for student in self.students:
            chanceInfected = ((studentsExpectedToInfect / numStudents)
                              + (teacherExpectedToInfect / numStudents * constants.TEACHER_STUDENT_MULTIPLIER)
                              + (teacherAssistantExpectedToInfect / numStudents * constants.TA_STUDENT_MULTIPLIER)) \
                            * student.infectivity
            newChanceInfected =