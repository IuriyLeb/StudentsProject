#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Selection of a random student for answer.

This module select random student in student group.
"""
import os
import random


def call_random_student_on_weight(student_list, __check_func_call_flag=1):
	"""
	Selection of random_student considering current weights
	Model of a comparison of the length of the segment of the probability to be answered
	Initially, every student get segment of length 10. After student's answer length of segment will be cut in half
	The boundaries of all segments are shifted
	input data: 1) student_list [name1,name2,...]
				2) __check_func_call_flag: flag needs for switching between initial and the next call

	output: return name of student in console
	"""
	student_dict = {ind: student for ind, student in enumerate(list_of_student, 1)}
	initial_weight = 100
	weight_changed = {}	
	weight = {i+1: [initial_weight * i, initial_weight * (i + 1)] for i in range(0, len(student_dict))}
	user_input = input("Press enter for working or q for exit..."+"\n")
	while user_input != "q":
		__check_func_call_flag = 0
		random_number = random.randint(2, weight[len(student_dict)][1])
		for key in weight:
			if weight[key][0] <= random_number < weight[key][1]:
				print student_dict[key]
				__check_func_call_flag = 1
				weight[key][1] -= weight_changed.get(key, initial_weight) / 2
				weight_changed[key] = weight[key][1] - weight[key][0]
				continue
			if __check_func_call_flag == 1:
				weight[key][0] = weight[key-1][1]
				weight[key][1] = weight[key][0] + weight_changed.get(key, initial_weight)
		user_input = input("Press q for exit..."+"\n" +"No if student isn't here" +"\n")
		if user_input == "No":
			del student_dict[key]
			del weight[key]
			actual_student_dict = {ind: student_dict[i] for ind, i in enumerate(sorted(student_dict.keys()), 1)}
			actual_weight = {ind: weight[i] for ind, i in enumerate(sorted(weight.keys()), 1)}
			__check_func_call_flag = 0
			break
	if __check_func_call_flag == 0:	
			call_random_student_on_weight(actual_student_dict, __check_func_call_flag)

