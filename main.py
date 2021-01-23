
import sys,os
from openpyxl import Workbook,load_workbook

def main():
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    directory = os.path.join(PROJECT_ROOT, 'OEC2021_-_School_Record_Book_.xlsx')
    wb = load_workbook(read_only=True, filename=directory)
    student_info = wb.sheetnames[0]
    teacher_info = wb.sheetnames[1]
    ta_info = wb.sheetnames[2]
    infected_info = wb.sheetnames[3]
    wb.close()

if __name__ == "__main__":
    try:
        main()
    finally:
        sys.exit(0)