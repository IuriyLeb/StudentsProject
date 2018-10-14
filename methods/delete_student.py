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


def delete(user_input, list_of_student, student_array=[]):
    try:
        student = random.choice(list_of_student)
        print(student)
        list_of_student.remove(student)
    except IndexError:
        sys.exit("You chose all students today!"
                 "Run again if you want to ask them second time!")
