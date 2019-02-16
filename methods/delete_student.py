import random
'''This module excludes the ability to select the same student twice in one session.'''


def delete_random_student(list_of_student: list, student_array=None):

    random_student = random.choice(list_of_student)
    list_of_student.remove(random_student)
    return random_student, student_array

