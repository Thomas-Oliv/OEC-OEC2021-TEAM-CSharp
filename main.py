
import sys,os
from openpyxl import Workbook, load_workbook
from Objects.Student import Student
from Objects.Teacher import Teacher
def main():
    students = list()
    teachers = list()
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
            infectivity = 0
            if student[9].value != 'N/A' and student[9].value is not None:
                extra_c = student[8].value.split(',')
            if student[8].value is not None and student[8].value != 'N/A':
                infectivity = 1
            students.append(Student(int(student[0].value), int(student[3].value), infectivity, classes, extra_c))

    teacher_info = wb[wb.sheetnames[1]]
    for teacher in teacher_info.iter_rows():
        if not any(teacher):
            break
        if isinstance(teacher[0].value, float) and teacher[0].value > 0:
            teachers.append(Teacher(int(teacher[0].value), teacher[3].value))

    wb.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
    finally:
        sys.exit(0)