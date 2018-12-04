<<<<<<< HEAD
<<<<<<< HEAD
import os
import random


def shift_one_segment(right_end, next_left_end, next_right_end):
    size = next_right_end - next_left_end
    left_end_new = right_end
    right_end_new = left_end_new + size
    return left_end_new, right_end_new


def shift_all_segment(ind_segment, weight=None):
    if weight is None:
        weight = []
    for ind in range(ind_segment, len(weight)):
        weight[ind][0], weight[ind][1] = shift_one_segment(weight[ind - 1][1], weight[ind][0],
                                                           weight[ind][1])
    return weight


def count_student_weight(list_of_student, weight=None):
    initial_weight = 100
    if weight is None:
        weight = [[initial_weight * i, initial_weight * (i + 1)] for i in range(len(list_of_student))]
    random_number = random.randint(2, sorted(weight)[-1][-1])
    for ind, segment in enumerate(weight):
        if segment[0] <= random_number <= segment[-1]:
            called_student = list_of_student[ind]
            ind_called_student = ind
            restrict_size = (weight[ind][1] - weight[ind][0]) // 2
            weight[ind][1] = weight[ind][1] - restrict_size
            weight = shift_all_segment(ind_called_student + 1, weight)
            return called_student, weight


if __name__ == '__main__':
    student_array = None
    list_of_student = []
    path_to_file_of_student = os.path.join(".", "data_input", "list_of_students.txt")
    with open(path_to_file_of_student, encoding="utf-8") as students_file:
        for line in students_file:
            student_name = line.strip().split(" ", 1)[1]
            list_of_student.append(student_name)
    while True:
        print('Press enter for choosing or q for exit...')
        user_input = input()
        if user_input == 'q':
            sys.exit("Lesson are finished! Good job!")
        called_student, student_array = count_student_weight(list_of_student, student_array)
        print(called_student)
=======
import os
import random


def shift_one_segment(right_end, next_left_end, next_right_end):
    size = next_right_end - next_left_end
    left_end_new = right_end
    right_end_new = left_end_new + size
    return left_end_new, right_end_new


def shift_all_segment(ind_segment, weight=None):
    for ind in range(ind_segment, len(weight)):
        weight[ind][0], weight[ind][1] = shift_one_segment(weight[ind - 1][1], weight[ind][0],
                                                           weight[ind][1])
    return weight


def count_student_weight(list_of_student, weight=None):
    initial_weight = 100
    if weight is None:
        weight = [[initial_weight * i, initial_weight * (i + 1)] for i in range(len(list_of_student))]
    random_number = random.randint(2, sorted(weight)[-1][-1])
    for ind, segment in enumerate(weight):
        if segment[0] <= random_number <= segment[-1]:
            called_student = list_of_student[ind]
            ind_called_student = ind
            restrict_size = (weight[ind][1] - weight[ind][0]) // 2
            weight[ind][1] = weight[ind][1] - restrict_size
            weight = shift_all_segment(ind_called_student + 1, weight)
            return called_student, weight


if __name__ == "__main__":
    student_array = None
    list_of_student = []
    path_to_file_of_student = os.path.join(".", "data_input", "list_of_students.txt")
    with open(path_to_file_of_student, encoding="utf-8") as students_file:
        for line in students_file:
            student_name = line.strip().split(" ", 1)[1]
            list_of_student.append(student_name)
    while True:
        print('Press enter for choosing or q for exit...')
        user_input = input()
        if user_input == 'q':
            sys.exit("Lesson are finished! Good job!")
        called_student, student_array = count_student_weight(list_of_student, student_array)
        print(called_student)
>>>>>>> Quotes consistency
=======
import os
import random
import sys


def shift_one_segment(right_end, next_left_end, next_right_end):
    size = next_right_end - next_left_end
    left_end_new = right_end
    right_end_new = left_end_new + size
    return left_end_new, right_end_new


def shift_all_segment(ind_segment, weight=None):
    for ind in range(ind_segment, len(weight)):
        weight[ind][0], weight[ind][1] = shift_one_segment(weight[ind - 1][1], weight[ind][0],
                                                           weight[ind][1])
    return weight


def count_student_weight(list_of_student, weight=None):
    initial_weight = 100
    if weight is None:
        weight = [[initial_weight * i, initial_weight * (i + 1)] for i in range(len(list_of_student))]
    random_number = random.randint(2, sorted(weight)[-1][-1])
    for ind, segment in enumerate(weight):
        if segment[0] <= random_number <= segment[-1]:
            called_student = list_of_student[ind]
            ind_called_student = ind
            restrict_size = (weight[ind][1] - weight[ind][0]) // 2
            weight[ind][1] = weight[ind][1] - restrict_size
            weight = shift_all_segment(ind_called_student + 1, weight)
            return called_student, weight


if __name__ == "__main__":
    student_array = None
    list_of_student = []
    path_to_file_of_student = os.path.join(".", "data_input", "list_of_students.txt")
    with open(path_to_file_of_student, encoding="utf-8") as students_file:
        for line in students_file:
            student_name = line.strip().split(" ", 1)[1]
            list_of_student.append(student_name)
    while True:
        print('Press enter for choosing or q for exit...')
        user_input = input()
        if user_input == 'q':
            sys.exit("Lesson are finished! Good job!")
        called_student, student_array = count_student_weight(list_of_student, student_array)
        print(called_student)
>>>>>>> fix some bag
