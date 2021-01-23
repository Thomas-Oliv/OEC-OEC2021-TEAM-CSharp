import constants
from Functions import computeNewChance


def extra_calc(students):
    #dictionary containing all extracurriculars
    extracurriculars = constants.EXTRACURRICULARS
    #add all students in extracurriculars to extracurricular dictionary
    for student in students:
        print(student.first)
        if student.extracurriculars is not None:
            extracurriculars[student.extracurriculars].append(student)
    #calculate increase in chance of disease for each extracurricular
    for key in extracurriculars:
        studentsExpectedToInfect = 0
        curricularSize = len(extracurriculars[key])
        for student in extracurriculars[key]:
            studentsExpectedToInfect += student.chanceOfDisease * constants.R_NAUGHT / constants.EXTRACURRICULAR_SPACING_FACTOR
        for student in extracurriculars[key]:
            chanceInfected = (studentsExpectedToInfect - student.chanceOfDisease) / curricularSize * student.infectivity
            student.chanceOfDisease = computeNewChance(student.chanceOfDisease, chanceInfected)
