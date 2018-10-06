# -*- coding: utf-8 -*-
"""OracleStudent.py.
This module presents methods of choosing random student
in a group to make easily for teacher to ask students
Methods:
    methods_one
Example:
        $ python OracleStudent.py -m method_1
"""
import argparse
import os
from methods import oracle_student

parser = argparse.ArgumentParser(description='Selection of random student for answer')
parser.add_argument("-in", "--path_to_file_of_student", default=os.path.join(".", "data_input", "list_of_student.txt"),
                    help='set path_to_file_of_student (default: data_input dir in dir with scripts)')
group = parser.add_mutually_exclusive_group()
group.add_argument("-m", "--name_method", action="store", help='name of random student method')

args = parser.parse_args()
if args.name_method:
    oracle_student.oracle(args.path_to_file_of_student, args.name_method)
