from methods.randomizer import choose_randomly
from methods.segments import count_student_weight
from methods.delete_student import delete_random_student
from methods.utils.mark_student import mark_student
import sys


def oracle(path_to_file_of_student, name_method, student_array=None):
    list_of_student = []
    choicer = {'randomizer': choose_randomly, 'segments': count_student_weight, 'delete_student': delete_random_student}
    with open(path_to_file_of_student, 'r', encoding='utf-8') as students_file:
        for line in students_file:
            student_name = line.strip().split(' ', 1)[1]
            list_of_student.append(student_name)
    print('Are all students here? Answer y/n')
    if input() == 'n':
        list_of_student = mark_student(list_of_student)
    while True:
        print('Press enter for choosing or q for exit...')
        user_input = input()
        if user_input == 'q':
            sys.exit('Lesson are finished! Good job!')
        called_student, student_array = choicer[name_method](list_of_student, student_array)
        print(called_student)
