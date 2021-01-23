import constants


def computeNewChance(originalChance, newChance) -> float:
    return min(1 - ((1 - originalChance) * (1 - newChance)), 1)


def extra_calc(students):
    extracurriculars = constants.EXTRACURRICULARS
    for student in students:
        print(student.first)
        if student.extracurriculars is not None:
            extracurriculars[student.extracurriculars].append(student)
    for key in extracurriculars:
        studentsExpectedToInfect = 0
        curricularSize = len(extracurriculars[key])
        for student in extracurriculars[key]:
            studentsExpectedToInfect += student.chanceOfDisease * 3
        for student in extracurriculars[key]:
            chanceInfected = (studentsExpectedToInfect / curricularSize) * student.infectivity
            student.chanceOfDisease = computeNewChance(student.chanceOfDisease, chanceInfected)
