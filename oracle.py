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


Example:
        python oracle.py -m name_of_method
"""
import argparse
import os
from methods import oracle_student

parser = argparse.ArgumentParser(description='Selection of random student for answer')
parser.add_argument('-i', '--path_to_file_of_student', default=os.path.join('.', 'data_input', 'list_of_students.txt'),
                    help='set path_to_file_of_student (default: data_input dir in dir with scripts)')
parser.add_argument('-n', '--name_method', action='store', required=True, choices=['randomizer', 'segments'],
                    help='enter name of random student method: method_1')

args = parser.parse_args()
if args.name_method:
    oracle_student.oracle(args.path_to_file_of_student, args.name_method)
