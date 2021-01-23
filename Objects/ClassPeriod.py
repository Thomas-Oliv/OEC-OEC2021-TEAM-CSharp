from typing import List

import constants

from Objects.TeachingAssistant import TeachingAssistant
from Objects.Student import Student
from Objects.Teacher import Teacher
from Functions import computeNewChance


class ClassPeriod:
    name: str
    period: int
    students: List[Student]
    ta: TeachingAssistant
    teacher: Teacher
    expectedInfectionsFromContamination: float

    def __init__(self, name, period, students, ta, teacher):
        self.name = name
        self.period = period
        self.students = students
        self.ta = ta
        self.teacher = teacher
        self.infectedMultiplier = 0

    def reducePeriod(self) -> float:
        """
        Calculates the new infection chance for each student, teacher, and TA in this class period\n
        Determines this probability by adding up expected values for number of students each person in the class
        is expected to infect based off an r0 value
        :return: the contamination value for the next class period
        """
        studentsExpectedToInfect = 0
        teacherExpectedToInfect = 0
        teacherAssistantExpectedToInfect = 0

        for student in self.students:
            # 3 is the r0 value
            studentsExpectedToInfect += student.chanceOfDisease * 3

        teacherExpectedToInfect += self.teacher.chanceInfected * 3
        teacherAssistantExpectedToInfect += self.ta.chanceInfected * 3

        classSize = len(self.students) + 2

        studentInfectionProbability = studentsExpectedToInfect / classSize
        teacherInfectionProbability = teacherExpectedToInfect / classSize
        teachersAssistantInfectionProbability = teacherAssistantExpectedToInfect / classSize
        contaminationInfectionProbability = self.expectedInfectionsFromContamination / classSize
        for student in self.students:
            chanceInfected = (studentInfectionProbability
                                + (teacherInfectionProbability * constants.TEACHER_STUDENT_MULTIPLIER)
                                + (teachersAssistantInfectionProbability * constants.TA_STUDENT_MULTIPLIER)
                                + contaminationInfectionProbability) \
                             * student.infectivity
            student.chanceOfDisease = computeNewChance(chanceInfected, student.chanceOfDisease)

        teacherChanceInfected = (studentInfectionProbability
                                 + (teacherInfectionProbability * constants.TEACHER_STUDENT_MULTIPLIER)
                                 + (teachersAssistantInfectionProbability * constants.TEACHER_TA_MULTIPLIER)
                                 + contaminationInfectionProbability)
        self.teacher.chanceInfected = computeNewChance(teacherChanceInfected, self.teacher.chanceInfected)

        taChanceInfected = (studentInfectionProbability
                            + (teacherInfectionProbability * constants.TEACHER_STUDENT_MULTIPLIER)
                            + (teachersAssistantInfectionProbability * constants.TEACHER_TA_MULTIPLIER)
                            + contaminationInfectionProbability)

        self.ta.chanceInfected = computeNewChance(taChanceInfected, self.ta.chanceInfected)

        # cleaning removes contamination
        if self.period == 2:
            return 0
        else:
            totalExpectedInfections = (studentsExpectedToInfect
                                       + teacherExpectedToInfect
                                       + teacherAssistantExpectedToInfect)
            return totalExpectedInfections * constants.CONTAMINATION_FACTOR
