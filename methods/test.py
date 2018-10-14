def func7(state={}):
    if not state:
        state[0]=0
    if state[0] > 2:
        state[0] = 0
    print(state[0])
    state[0] += 1

for i in range(9):
    func7()  # 0

# -*- coding: utf-8 -*-

"""Selection of a random student for answer.

This module select random student in student group.
"""
import os
import random
import sys


def shift_one_segment(right_end, next_left_end, next_right_end):
    """
     Moving borders of current segment along line

     input data: int: 1) right_end, next_left_end, next_right_end - ends previous
                    and current segment
     output: return new borders
     """
    size = next_right_end - next_left_end
    left_end_new = right_end
    right_end_new = left_end_new + size
    return (left_end_new, right_end_new)

def shift_all_segment(ind_segment, weight=[]):
    for ind in range(ind_segment, len(weight)):
        weight[ind][0], weight[ind][1] = shift_one_segment(weight[ind - 1][1], weight[ind][0],
                                                       weight[ind][1])
    return weight
'''
def call_random_student_on_weight(student_list, weight=[], _check_call_func_flag=1):
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
    if not weight:
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

def random_student(list_of_student, student_dict={}):
    print('are all students here? Answer y/n')
    x = input()
    if x == 'n':
        delete_absent_student(list_of_student)
    while True:
        student_dict = check_student_status(user_input,list_of_student,student_dict)

'''
def call_random_student_on_weight(student_list, weight=[]):
    initial_weight = 100
    if not weight:
        weight = [[initial_weight * i, initial_weight * (i + 1)] for i in range(len(student_list))]
    while True:
        print('Choose a random student? y/n/')
        user_input = input()
        if user_input == "y":
            random_number = random.randint(2, sorted(weight)[-1][-1])
            for ind, segment in enumerate(weight):
                if segment[0] <= random_number <= segment[-1]:
                    called_student = student_list[ind]
                    ind_called_student = ind
                    print(called_student, ind)
                    break
            user_input = input("\n enter  No if student isn't here  \n")
            if user_input == "No":
                student_list.remove(called_student)
                del weight[ind_called_student]
                shift_all_segment(ind_called_student + 1, weight)
                break
            else:
                restrict_size = (weight[ind][1] - weight[ind][0]) // 2
                weight[ind][1] = weight[ind][1] - restrict_size
                shift_all_segment(ind_called_student, weight)
            call_random_student_on_weight(student_list, weight)
        else:
            sys.exit()

