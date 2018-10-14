import random
import sys


def delete_absent_student(list_of_student):
    for i in range(len(list_of_student)):
        print(i+1, list_of_student[i])
    print('who is absent today? print their №')
    try:
        absent_student = [int(i) for i in input().split()]
        for number_of_student in range(len(absent_student)):
            list_of_student.remove(list_of_student[number_of_student])
    except ValueError:
        print("Please enter correct integer number of student")
        delete_absent_student(list_of_student)


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

"""
def random_student(list_of_student, student_dict={}):
    print('are all students here? Answer y/n')
    x = input()
    if x == 'n':
        delete_absent_student(list_of_student)
    while True:
        print('Choose a random student? y/n')
        user_input = input()
        student_dict = check_student_status(user_input,list_of_student,student_dict)
        print(student_dict)
"""






