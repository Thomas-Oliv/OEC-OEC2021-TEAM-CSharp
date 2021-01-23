
import sys,os
from openpyxl import Workbook, load_workbook
from Objects.Student import Student

def main():
    students = list()
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    directory = os.path.join(PROJECT_ROOT, 'OEC2021_-_School_Record_Book_.xlsx')
    wb = load_workbook(read_only=True, filename=directory)
    student_info = wb[wb.sheetnames[0]]
    for key, *student in student_info.iter_rows():
        if key.value is None:
            break
        if isinstance(key.value, float) and key.value > 0:
            classes = [student[3].value, student[4].value, student[5].value, student[6].value]
            extra_c = None
            if student[8].value != 'N/A':
                extra_c = student[8].value.split(',')
            infectivity = 1
            if student[7].value is not None:
                infectivity += 0.7
            tmp = Student(int(key.value), student[2].value, infectivity, classes, extra_c)
            students.append(Student(int(key.value), student[2].value, infectivity, classes, extra_c))



    wb.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
    finally:
        sys.exit(0)