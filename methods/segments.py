import random

'''This module decrease the probability to select the same student twice in one session.'''


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
