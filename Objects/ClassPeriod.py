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
        self.expectedInfectionsFromContamination = 0

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

        # Calculate the number of people expected to be infected by each type of person (student, teacher, ta)
        for student in self.students:
            # 3 is the r0 value
            studentsExpectedToInfect += student.chanceOfDisease * 3

        teacherExpectedToInfect += self.teacher.chanceInfected * 3
        teacherAssistantExpectedToInfect += self.ta.chanceInfected * 3 if self.ta is not None else 0

        classSize = len(self.students) + 2

        studentInfectionProbability = studentsExpectedToInfect / classSize
        teacherInfectionProbability = teacherExpectedToInfect / classSize
        teachersAssistantInfectionProbability = teacherAssistantExpectedToInfect / classSize
        contaminationInfectionProbability = self.expectedInfectionsFromContamination / classSize

        # Recalculate chanceInfected for each person
        # Based on the percent chance that each group with infect anyone (regardless of group)
        # Add infectionProbability for each group and multiply
        for student in self.students:
            chanceInfected = (studentInfectionProbability
                                + (teacherInfectionProbability * constants.TEACHER_STUDENT_MULTIPLIER)
                                + (teachersAssistantInfectionProbability * constants.TA_STUDENT_MULTIPLIER)
                                + contaminationInfectionProbability
                                - student.chanceOfDisease / classSize) \
                             * student.infectivity
            student.chanceOfDisease = computeNewChance(chanceInfected, student.chanceOfDisease)

        teacherChanceInfected = (studentInfectionProbability * constants.TEACHER_STUDENT_MULTIPLIER
                                 + (teachersAssistantInfectionProbability * constants.TEACHER_TA_MULTIPLIER)
                                 + contaminationInfectionProbability
                                 - self.teacher.chanceInfected / classSize)
        self.teacher.chanceInfected = computeNewChance(teacherChanceInfected, self.teacher.chanceInfected)

        taChanceInfected = (studentInfectionProbability * constants.TA_STUDENT_MULTIPLIER
                            + (teacherInfectionProbability * constants.TEACHER_STUDENT_MULTIPLIER)
                            + contaminationInfectionProbability
                            - self.ta.chanceInfected / classSize)
        if self.ta is not None:
            self.ta.chanceInfected = computeNewChance(taChanceInfected, self.ta.chanceInfected)

        # cleaning removes contamination
        # Return totalExpectedInfections for the next period to use
        if self.period == 2:
            return 0
        else:
            totalExpectedInfections = (studentsExpectedToInfect
                                       + teacherExpectedToInfect
                                       + teacherAssistantExpectedToInfect)
            return totalExpectedInfections * constants.CONTAMINATION_FACTOR
