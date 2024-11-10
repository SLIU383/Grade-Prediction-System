import numpy as np

def merge_grades(input_data):
    _merge_grade = []
    for item in input_data:
        if item == 'A' or item == 'A+' or item == 'A-':
            _merge_grade.append("A")
        elif item == 'B' or item == 'B+' or item == 'B-':
            _merge_grade.append("B")
        elif item == 'C' or item == 'C+' or item == 'C-':
            _merge_grade.append("C")
        elif item == 'D' or item == 'D+' or item == 'D-':
            _merge_grade.append("D")
    return np.array(_merge_grade)