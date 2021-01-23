import constants
from Objects.Student import Student
from typing import List


def extra_calc(students):
    extracurriculars = constants.EXTRACURRICULARS
    for student in students:
        for extra in student.extracurriculars:
            extracurriculars[extra].append(student)
