# -*- coding: utf-8 -*-
"""oracle.py.
This module presents methods of choosing random student
in a group to make easily for teacher to ask students
Methods:
    1)segments: selection of random_student considering current weights
        Model of a comparison of the length of the segment of the probability to be answered
        Initially, every student get segment of length 100.
        After student's answer length of segment will be cut in half
        The boundaries of all segments are shifted

    2)randomizer: selection of random student considering number of times
        student answer. Initially, every student gets zero point.
        Student who is asked gets one point and can not be
        choose the second time in row, after it point returt to zero

    3)delete: selection random of student excluding student who is
        answered on every step.


Usage:
        python oracle.py -m '1', '2' or '3' 1:segments, 2:randomizer, 3:delete_student
"""
import argparse
import os
from methods.utils.oracle_student import oracle

choices = {'1': 'randomizer', '2': 'segments', '3': 'delete_student'}
parser = argparse.ArgumentParser(description='Selection of random student for answer')
parser.add_argument('-i', '--path_to_file_of_student', default=os.path.join('.', 'data_input', 'list_of_students.txt'),
                    help='set path_to_file_of_student (default: data_input dir in dir with scripts)')
parser.add_argument('-n', '--name_method', action='store', required=True, choices=['1', '2', '3'],
                    help='enter number of random student method: 1:randomizer, 2:segments, 3:delete_student')

args = parser.parse_args()
if args.name_method:
    oracle(args.path_to_file_of_student, choices[args.name_method])
