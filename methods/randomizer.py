import random
'''This module reduces the probability of choosing the same student twice in a row by tagging the called one. '''


def choose_randomly(list_of_students: list, student_array=None):
    if not student_array:
        student_array = {}
    for student in list_of_students:
        random_student = random.choice(list_of_students)
        student_array[random_student] = 0
        if student_array[random_student]:
            random_student = random.choice(list_of_students)
            student_array[random_student] = 0
            student_array[random_student] += 1
        return random_student, student_array
