from typing import List, Dict
from Objects.Student import Student
from Objects.Teacher import Teacher
from Objects.TeachingAssistant import TeachingAssistant

from Objects.ClassPeriod import ClassPeriod
from Objects.Lunch import Lunch
from Objects.ExtraCurricular import ExtraCurricular


class Directory:
    teachers: List[Teacher]
    students: List[Student]
    teachingAssistants: List[TeachingAssistant]
    """
    {
        [period number/lunch]: {
            [className/grade]: ClassPeriod/Lunch
        }
    }
    """
    periodDict: Dict

    def __init__(self, teachers, students, tas):
        self.teachers = teachers
        self.teachingAssistants = tas
        self.students = students
        periodDict = {
            1: {},
            2: {},
            'Lunch': {},
            3: {},
            4: {},
        }
        classToTeacherMap = {
            teacher.classTeaching: teacher for teacher in teachers
        }
        # generates period dict with dict of classes for each period
        # maps from period to classes, in the case of the lunch period it maps by grade level
        for student in students:
            for period in periodDict.keys():
                if period == 'Lunch':
                    if student.grade not in periodDict[period]:
                        periodDict[period][student.grade] = Lunch([student])
                    else:
                        periodDict[period][student.grade].students.append(student)
                else:
                    currentClass = student.classes[period - 1]
                    taForClass = None
                    for ta in self.teachingAssistants:
                        if ta.classes[period - 1] == currentClass:
                            taForClass = ta
                    teacherOfClass = classToTeacherMap[currentClass]

                    if currentClass not in periodDict[period]:
                        periodDict[period][currentClass] = ClassPeriod(currentClass, 1, [student], taForClass,
                                                                       teacherOfClass)
                    else:
                        periodDict[period][currentClass].students.append(student)

        self.periodDict = periodDict

    def reducePeriod(self, periodNumber):
        """
        Calls the reduce method for each ClassPeriod/Lunch/Extracurricular object for a given period
        :param periodNumber: the period for which to run calculations on, also accepts lunch/extra
        :return: None
        """
        if periodNumber == 'Extra':
            ExtraCurricular(self.students).reduce()
            return
        currentPeriod = self.periodDict[periodNumber]
        if periodNumber == 'Lunch':
            for grade in currentPeriod.keys():
                currentPeriod[grade].reduce()
        else:
            for className in currentPeriod.keys():
                infectionNumber = currentPeriod[className].reducePeriod()
                if currentPeriod == 1 or currentPeriod == 3:
                    nextPeriodClass = self.periodDict[currentPeriod + 1][className]
                    nextPeriodClass.expectedInfectionsFromContamination = infectionNumber
