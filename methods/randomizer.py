import random
import sys


def check_student_status(user_input,list_of_student, student_dict={}):
    if user_input == 'y':
        somestud = random.choice(list_of_student)
        if not student_dict:
            student_dict = {student: 0 for student in list_of_student}
        if student_dict[somestud] > 0:
            somestud = random.choice(list_of_student)
            student_dict[somestud] = 0
        print(somestud)
        student_dict[somestud] += 1
        return student_dict
    elif user_input == 'n':
        sys.exit("Lesson are finished! Good job!")
