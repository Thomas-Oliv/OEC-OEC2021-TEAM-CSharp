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

    @staticmethod
    def computeNewChance(originalChance, newChance) -> float:
        return min(1 - ((1 - originalChance) * (1 - newChance)), 1)

    def reducePeriod(self):
        studentsExpectedToInfect = 0
        teacherExpectedToInfect = 0
        teacherAssistantExpectedToInfect = 0

        for student in self.students:
            # 3 is the r0 value
            studentsExpectedToInfect += student.chanceOfDisease * 3

        teacherExpectedToInfect += self.teacher.chanceInfected * 3
        teacherAssistantExpectedToInfect += self.ta.chanceInfected * 3

        classSize = len(self.students) + 2
        for student in self.students:
            # TODO figure out from contamination value
            chanceInfected = ((studentsExpectedToInfect / classSize)
                              + (teacherExpectedToInfect / classSize * constants.TEACHER_STUDENT_MULTIPLIER)
                              + (teacherAssistantExpectedToInfect / classSize * constants.TA_STUDENT_MULTIPLIER)) \
                             * student.infectivity
            student.chanceOfDisease = ClassPeriod.computeNewChance(chanceInfected, student.chanceOfDisease)

        teacherChanceInfected = ((studentsExpectedToInfect / classSize)
                                 + (teacherExpectedToInfect / classSize * constants.TEACHER_STUDENT_MULTIPLIER)
                                 + (teacherAssistantExpectedToInfect / classSize * constants.TEACHER_TA_MULTIPLIER))
        self.teacher.chanceInfected = ClassPeriod.computeNewChance(teacherChanceInfected, self.teacher.chanceInfected)

        taChanceInfected = ((studentsExpectedToInfect / classSize)
                                 + (teacherExpectedToInfect / classSize * constants.TEACHER_STUDENT_MULTIPLIER)
                                 + (teacherAssistantExpectedToInfect / classSize * constants.TEACHER_TA_MULTIPLIER))
        self.ta.chanceInfected = ClassPeriod.computeNewChance(taChanceInfected, self.ta.chanceInfected)

        # TODO figure out how to compute new contamination

        # cleaning removes contamination
        if self.period == 2:
            self.contaminationMultiplier = 0
