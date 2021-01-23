from typing import List
from Objects.Student import Student
from Objects.Teacher import Teacher
from Objects.TeachingAssistant import TeachingAssistant


class Directory:
    Teachers: List[Teacher]
    Students: List[Student]
    TeachingAssistants: List[TeachingAssistant]

    def __init__(self, teachers, students, ta):
        self.Teachers = teachers
        self.TeachingAssistants = ta
        self.Students = students
