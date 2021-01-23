from typing import List

from Objects.TeachingAssistant import TeachingAssistant
from Objects.Student import Student
from Objects.Teacher import Teacher


class ClassPeriod:
    name: str
    period: int
    students: List[Student]
    ta: TeachingAssistant
    teacher: Teacher

    def __init__(self, name, period, students, ta, teacher):
        self.name = name
        self.period = period
        self.students = students
        self.ta = ta
        self.teacher = teacher
