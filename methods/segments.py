# -*- coding: utf-8 -*-

"""Selection of a random student for answer.

This module select random student in student group.
"""
import os
import random


def shift_one_segment(right_end, next_left_end, next_right_end):
    size = next_right_end - next_left_end
    left_end_new = right_end
    right_end_new = left_end_new + size
    return (left_end_new, right_end_new)


def shift_all_segment(ind_segment, weight=[]):
    for ind in range(ind_segment, len(weight)):
        weight[ind][0], weight[ind][1] = shift_one_segment(weight[ind - 1][1], weight[ind][0],
                                                       weight[ind][1])
        return weight

def count_student_weight(user_input,list_of_student, weight=[]):
    initial_weight = 10
    flag = 0
    if not weight:
        weight = [[initial_weight * i, initial_weight * (i + 1)] for i in range(len(list_of_student))]
    random_number = random.randint(2, sorted(weight)[-1][-1])
    for ind, segment in enumerate(weight):
        if segment[0] <= random_number <= segment[-1]:
            called_student = list_of_student[ind]
            ind_called_student = ind
            print(called_student, ind)
            if delete_student_during_call(list_of_student, weight, ind_called_student):
                return(weight)
            restrict_size = (weight[ind][1] - weight[ind][0]) // 2
            weight[ind][1] = weight[ind][1] - restrict_size
            flag = 1
        elif flag == 1:
            weight =  shift_all_segment(ind_called_student, weight)
    return(weight)


def delete_student_during_call(list_of_student, weight, ind_called_student):
    user_input = input("\n enter  No if student isn't here  \n")
    if user_input == "No":
        del list_of_student[ind_called_student]
        del weight[ind_called_student]
        shift_all_segment(ind_called_student + 1, weight)
        return weight
    else:
        return False
