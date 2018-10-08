# -*- coding: utf-8 -*-

"""Selection of a random student for answer.

This module select random student in student group.
"""
import os
import random


def shift_segment(right_end, next_left_end, next_right_end):
    """
     Moving borders of current segment along line

     input data: int: 1) right_end, next_left_end, next_right_end - ends previous
                    and current segment
     output: return new
     """
    size = next_right_end - next_left_end
    left_end_new = right_end
    right_end_new = left_end_new + size
    return (left_end_new, right_end_new)


def call_random_student_on_weight(student_list, weight=[], _check_call_func_flag=1):
    print(student_list)
    """
    Selection of random_student considering current weights
    Model of a comparison of the length of the segment of the probability to be answered
    Initially, every student get segment of length 100. After student's answer length of segment will be cut in half
    The boundaries of all segments are shifted
    input data: list: 1) student_list [name1,name2,...]
    			int:  2) _check_call_func_flag: flag needs for switching between initial and the next call
    output: return new borders of segment
    """
    initial_weight = 100
    if _check_call_func_flag == 1:
        weight = [[initial_weight * i, initial_weight * (i + 1)] for i in range(len(student_list))]
    user_input = input("Press enter for working or q for exit...\n")
    while user_input != "q":
        _check_call_func_flag = 0
        random_number = random.randint(2, sorted(weight)[-1][-1])
        for ind, segment in enumerate(weight):
            if segment[0] <= random_number <= segment[-1]:
                called_student = student_list[ind]
                ind_called_student = ind
                print(called_student)
                user_input = input("Press q for exit...  \n  No if student isn't here  \n")
                if user_input == "No":
                    break
                restrict_size = (weight[ind][1] - weight[ind][0]) // 2
                weight[ind][1] = weight[ind][1] - restrict_size
                _check_call_func_flag = 1
            elif _check_call_func_flag == 1:
                weight[ind][0], weight[ind][1] = shift_segment(weight[ind - 1][1], weight[ind][0], weight[ind][1])
        if _check_call_func_flag == 0:
            student_list.remove(called_student)
            del weight[ind_called_student]
            for ind in range(ind_called_student + 1, len(weight)):
                weight[ind][0], weight[ind][1] = shift_segment(weight[ind - 1][1], weight[ind][0], weight[ind][1])
            break
    if (_check_call_func_flag == 0) and (user_input != "q"):
        call_random_student_on_weight(student_list, weight, _check_call_func_flag)


if __name__ == '__main__':
    list_of_student = []
    path_to_file_of_student = os.path.join(".", "data_input", "list_of_students.txt")
    with open(path_to_file_of_student, "rb") as students_file:
        for line in students_file:
            student_name = line.decode("utf-8").strip().split(" ", 1)[1]
            list_of_student.append(student_name)
    student_dict = {ind: student for ind, student in enumerate(list_of_student, 1)}
    call_random_student_on_weight(list_of_student)
