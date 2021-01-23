
import sys,os
from openpyxl import Workbook, load_workbook
from Objects.Student import Student
from Objects.Teacher import Teacher
from Objects.TeachingAssistant import TeachingAssistant

def main():
    students = list()
    teachers = list()
    tas = list()
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    directory = os.path.join(PROJECT_ROOT, 'OEC2021_-_School_Record_Book_.xlsx')
    wb = load_workbook(read_only=True, filename=directory)
    student_info = wb[wb.sheetnames[0]]
    for student in student_info.iter_rows():
        if not any(student):
            break
        if isinstance(student[0].value, float) and student[0].value > 0:
            classes = [student[4].value, student[5].value, student[6].value, student[7].value]
            extra_c = None
            health_problem = False
            if student[9].value != 'N/A' and student[9].value is not None:
                extra_c = student[9].value.split(',')[0]
            if student[8].value is not None and student[8].value != 'N/A':
                health_problem = True
            students.append(Student(int(student[0].value), student[2].value, student[1].value, int(student[3].value), health_problem, classes, extra_c))

    teacher_info = wb[wb.sheetnames[1]]
    for teacher in teacher_info.iter_rows():
        if not any(teacher):
            break
        if isinstance(teacher[0].value, float) and teacher[0].value > 0:
            teachers.append(Teacher(int(teacher[0].value), teacher[2].value, teacher[1].value, teacher[3].value))

    ta_info = wb[wb.sheetnames[2]]
    for ta in ta_info.iter_rows():
        print(ta)
        if not any(ta):
            break
        if isinstance(ta[0].value, float) and ta[0].value > 0:
            classes = [ta[2].value, ta[3].value, ta[4].value, ta[5].value]
            tas.append(TeachingAssistant(ta[1].value,ta[0].value, classes))



    wb.close()

if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
    finally:
        sys.exit(0)