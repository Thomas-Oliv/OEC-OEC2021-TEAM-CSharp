from Objects.Student import Student
from typing import List


class Extracurricular:
    students: List[Student]
    name: str

    def __init__(self, name):
        self.name = name,
        self.students = []
